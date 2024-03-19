import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

class Config:
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY_DEV")

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI_SQLITE")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=1)


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY_PRODUCTION")

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI_MYSQL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
