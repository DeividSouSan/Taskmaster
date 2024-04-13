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

    def get_tasks(self, user_id: int):
        with Session(self.__engine) as session:
            tasks = session.query(Task).filter(Task.user_id == user_id)
            return tasks

    def get_task_by_id(self, task_id: int):
        with Session(self.__engine) as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            return task

    def get_tasks_like(self, user_id: int, text: str):
        with Session(self.__engine) as session:
            print(text)
            tasks = session.query(Task).filter(
                Task.user_id == user_id, Task.title.like(f"%{text}%")
            )
            return tasks

    def update_task(self, task_id: int, values: dict[str, any]):

        with Session(self.__engine) as session:
            row_matched = session.query(Task).filter(Task.id == task_id).update(values)
            print(row_matched)
            session.commit()

    def delete_task(self, task_id: int):
        with Session(self.__engine) as session:
            task = session.query(Task).filter(Task.id == task_id).first()

            if task is not None:
                session.delete(task)

            session.commit()
