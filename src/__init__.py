from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_htmx import HTMX
from flask_wtf import CSRFProtect
from datetime import timedelta


# Initialize Plugins
db = SQLAlchemy()
login_manager = LoginManager()
htmx = HTMX()
csrf = CSRFProtect()


def create_app():
    # Creating App
    app = Flask(__name__)

    # Configuring App
    app.config.from_object('src.config.DevelopmentConfig')

    # Initializing Plugins
    db.init_app(app)
    login_manager.init_app(app)
    htmx.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        # Create tables
        from .models.task import Task  # pylint: disable=unused-import
        from .models.user import User  # pylint: disable=unused-import

        db.create_all()

        # Register Routes
        from .routes import auth_routes, view_routes, task_routes, form_routes
        app.register_blueprint(task_routes.task)
        app.register_blueprint(auth_routes.auth)
        app.register_blueprint(view_routes.view)
        app.register_blueprint(form_routes.form)

    return app
