import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY_DEV")
    
    db_path = os.path.join(os.path.dirname(__file__), 'taskmaster.db')
    db_uri = f'sqlite+pysqlite:///{db_path}'
    SQLALCHEMY_DATABASE_URI = db_uri
    
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)


class TestingConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY_TEST")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI_SQLITE_TEST")
    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=10)


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY_PROD")
    
    db_path = os.path.join(os.path.dirname(__file__), 'taskmaster.db')
    db_uri = f'sqlite+pysqlite:///{db_path}'
    SQLALCHEMY_DATABASE_URI = db_uri
    
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
