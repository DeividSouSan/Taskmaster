from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@localhost/{DATABASE}'


def create_app(test_config=None):
    app = Flask(__name__,
                template_folder="../templates",
                static_folder="../static",
                instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE_URI=DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    if app.config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from ..routes import routes
    app.register_blueprint(routes.bp)

    return app
