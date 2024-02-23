from flask_sqlalchemy import SQLAlchemy
from flask import current_app


db = SQLAlchemy()


def initialize_database():
	with current_app.app_context():
		db.init_app(current_app)


def create_database():
	from src.models.task import Task  # pylint: disable=unused-import
	from src.models.user import User  # pylint: disable=unused-import

	with current_app.app_context():
		db.create_all()
		print("As tabelas 'user' e 'task' foram criadas com sucesso.")
