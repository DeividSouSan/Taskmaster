from datetime import timedelta

from flask import Flask
from flask_htmx import HTMX
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# Initialize Plugins
db = SQLAlchemy()
login_manager = LoginManager()
htmx = HTMX()
csrf = CSRFProtect()


def create_app(config: str):
    # Creating App
    app = Flask(__name__)

    # Configuring App
    app.config.from_object(f"src.config.{config}")

    # Initializing Plugins
    login_manager.init_app(app)
    htmx.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from src.routes.router import api

        app.register_blueprint(api)

    return app
