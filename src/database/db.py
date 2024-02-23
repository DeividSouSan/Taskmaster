from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Database():
    def __init__(self, app):
        self.app = app

    def initialize_database(self):
        db.init_app(self.app)

    def create_tables(self):
        from ..models.task import Task  # pylint: disable=unused-import
        from ..models.user import User  # pylint: disable=unused-import

        with self.app.app_context():
            db.create_all()

        print("As tabelas 'user' e 'task' foram criadas com sucesso.")
