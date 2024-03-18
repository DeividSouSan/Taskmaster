import os
from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_htmx import HTMX
from datetime import timedelta

load_dotenv()

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@localhost/{DATABASE}'

# Initialize Plugins
db = SQLAlchemy()
login_manager = LoginManager()
htmx = HTMX()
# CSRF_TOKEN


def create_app():
    # Creating App
    app = Flask(__name__,
                template_folder="templates",
                static_folder="static",
                instance_relative_config=True)

    # Configuring App
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        PERMANENT_SESSION_LIFETIME=timedelta(minutes=30)
    )

    # Initializing Plugins
    db.init_app(app)
    login_manager.init_app(app)
    htmx.init_app(app)

    with app.app_context():
        # Create tables
        from .models.task import Task  # pylint: disable=unused-import
        from .models.user import User  # pylint: disable=unused-import

        db.create_all()

        # Register Routes
        from .routes import user_routes, auth_routes, main_routes
        app.register_blueprint(user_routes.user)
        app.register_blueprint(auth_routes.auth)
        app.register_blueprint(main_routes.main)

    return app
