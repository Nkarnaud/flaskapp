# config.py
import os

class Config:
    """
    Application configuration
    """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'p9Bv<3Eid9%$ju452i01'
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 0

    # Put any configurations for our application


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = 'mysql://sa_admin:sa_admin@localhost/smartanalytica_db'
    DEBUG_TB_ENABLED = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

class TestConfig(Config):
    """
    Test configurations
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://sa_admin:sa_admin@localhost/smartanalytica_db'
    BCRYPT_LOG_ROUNDS = 4
    TOKEN_EXPIRATION_DAYS = 0
    TOKEN_EXPIRATION_SECONDS = 3


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'test': TestConfig
}