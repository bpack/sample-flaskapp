import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SAMPLE_MESSAGE = 'Sample application running'

class DevelopmentConfig(Config):
    DEBUG = True
    SAMPLE_MESSAGE = 'Sample application running in development mode'

class ProductionConfig(Config):
    pass

by_name = dict(
    dev = DevelopmentConfig,
    prod = ProductionConfig
)


