from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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

    def get_active_tasks(self, user_id: int):
        with Session(self.__engine) as session:
            tasks = session.query(Task).filter(
                Task.user_id == user_id, Task.deleted == False
            )
            return tasks

    def get_task_by_id(self, task_id: int):
        with Session(self.__engine) as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            return task

    def get_tasks_like(self, user_id: int, text: str):
        with Session(self.__engine) as session:
            print(text)
            tasks = session.query(Task).filter(
                Task.user_id == user_id,
                Task.title.like(f"%{text}%"),
                Task.deleted == False,
            )
            return tasks

    def get_deleted_tasks(self, user_id: int):
        with Session(self.__engine) as session:
            tasks = session.query(Task).filter(
                Task.user_id == user_id, Task.deleted == True
            )
            return tasks

    def update_task(self, task_id, columns, value):
        with Session(self.__engine) as session:
            session.query(Task).filter(Task.id == task_id).update({columns: value})
            session.commit()

    def move_to_trash(self, task_id: int):
        with Session(self.__engine) as session:
            session.query(Task).filter(Task.id == task_id).update({Task.deleted: True})
            session.commit()
