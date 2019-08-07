import os

class Config:
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):

    pass

class  DevConfig(Config):
    DEBUG = True

    config_aptions = {
        'development': DevConfig,
        'production':ProdConfig
    }