import os

class Config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DB_URI = 'postgresql+psycopg2://test:test@localhost:5432/test'

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DB_URI = os.environ.get('SQLALCHEMY_DB_URI')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
