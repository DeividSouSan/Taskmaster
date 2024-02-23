from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager
import os

from ..database.db import Database
from ..models.user import User

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
        SQLALCHEMY_DATABASE_URI=DATABASE_URI,
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

    from ..database import db
    db = Database(app)
    db.initialize_database()
    db.create_tables()

    from ..routes import routes
    app.register_blueprint(routes.bp)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "website.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
