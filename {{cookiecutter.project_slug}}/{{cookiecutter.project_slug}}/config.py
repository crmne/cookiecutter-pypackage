# -*- coding: utf-8 -*-
from yconf import BaseConfiguration


class Config(BaseConfiguration):

    def __init__(self, **kwargs):
        # Overridden initializer that sets a default config path
        super(Config, self).__init__(**kwargs)
        self.configPath = "config.yaml"
