from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import current_app
from src.models.task import Task


class TaskRepository:
    def __init__(self):
        with current_app.app_context():
            DATABASE_URI = current_app.config["SQLALCHEMY_DATABASE_URI"]

        self.__engine = create_engine(DATABASE_URI)

    def add_task(self, task: Task):
        with Session(self.__engine) as session:
            session.add(task)
            session.commit()
