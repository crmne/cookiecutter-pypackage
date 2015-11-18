from setuptools.command.install import install


class CustomInstall(install):
    """Customized setuptools install command.

    Installs git submodules and packages that need to be installed first."""
    files = {
        'install_first': 'requirements_install_first.txt',
        'submodules': 'requirements_submodules.txt'
    }

    @staticmethod
    def _read_requirements(filename):
        with open(filename, 'r') as f:
            return [l.strip() for l in f.readlines()]

    def run(self):
        import os
        import pip
        from distutils.sysconfig import get_python_lib

        self.requirements = {k: self._read_requirements(v)
                             for k, v in self.files.items()}

        for package in self.requirements['install_first']:
            pip.main(['install', package])

        install.do_egg_install(self)

        current_dir = os.path.dirname(os.path.realpath(__file__))
        for submodule in self.requirements['git_submodules']:
            pth_path = os.path.join(get_python_lib(), submodule + ".pth")
            with open(pth_path, 'w') as pth:
                pth.write(os.path.join(current_dir, submodule) + os.linesep)


def read_requirements(filename):
    from pip.req import parse_requirements
    from pip.download import PipSession
    install_reqs = parse_requirements(filename, session=PipSession())
    return [str(ir.req) for ir in install_reqs]
