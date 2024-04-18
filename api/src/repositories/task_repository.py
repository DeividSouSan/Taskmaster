from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.models.task import Task


class TaskRepository:
    """
    Repository Class for the Task model.

    Responsible for handling the database operations for the Task model. It has methods for adding, getting, updating and deleting tasks from the database.

    The SQLALCHEMY_DATABASE_URI is obtained from the current_app.config, which is the configuration of the Flask application. This way, the repository can be used in the application context.

    If you want to change the database, you can change the SQLACLHEMY_DATABASE_URI in the configuration file of the application config.py.

    Attributes:
        _engine: The SQLAlchemy engine that connects to the database.
    """

    def __init__(self):
        with current_app.app_context():
            DATABASE_URI = current_app.config["SQLALCHEMY_DATABASE_URI"]

        self._engine = create_engine(DATABASE_URI)

    def add_task(self, task: Task) -> bool:
        """
        Adds a task to the database.

        Througn the session context manager, it adds the task to the database and commits the transaction.

        Args:
            task: The Task object to be added to the database.

        Returns:
            bool: True if the task was added successfully, False otherwise.
        """
        with Session(self._engine) as session:
            # TODO: improve the exception handling, and return.

            try:
                session.add(task)
                session.commit()

                return True
            except:
                return False

    def get_tasks(self, user_id: int):
        """
        Get all tasks from the database.

        Through the session context manager, it queries the database for all tasks of a specific user.

        Args:
            user_id: The id of the user that owns the tasks.

        Returns:
            Query[Task]: A list with all tasks of the user.
        """
        with Session(self._engine) as session:
            tasks = session.query(Task).filter(Task.user_id == user_id)
            return tasks

    def get_task_by_id(self, task_id: int):
        """
        Query the database for a task by its id.

        Through the session context manager, it queries the database for a task with a specific id.

        Args:
            task_id: The id of the task to be queried.

        Returns:
            Task: The task with the id task_id.
        """
        with Session(self._engine) as session:
            task = session.query(Task).filter(Task.id == task_id).first()
            return task

    def get_tasks_like(self, user_id: int, text: str):
        """
        Query the database for tasks that have a specific text in the title.

        Through the session context manager, it queries the database for tasks of a specific user that have a specific text in the title.

        Args:
            user_id: The id of the user that owns the tasks.
            text: The text that the title of the tasks must contain.

        Returns:
            Query[Task]: A list with all tasks of the user that have the text in the title.
        """
        with Session(self._engine) as session:
            tasks = session.query(Task).filter(
                Task.user_id == user_id, Task.title.like(f"%{text}%")
            )
            return tasks

    def update_task(self, task_id: int, values: dict[str, any]) -> bool:
        """
        Update a task in the database.

        Through the session context manager, it updates a task in the database with the values in the dictionary.

        Args:
            task_id: The id of the task to be updated.
            values: A dictionary with the values to be updated.

        Returns:
            bool: True if the task was updated successfully, False otherwise.
        """
        with Session(self._engine) as session:
            # TODO: improve the exception handling, and return.
            try:
                session.query(Task).filter(Task.id == task_id).update(values)
                session.commit()

                return True
            except:
                return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the database.

        Through the session context manager, it deletes a task from the database.

        Args:
            task_id: The id of the task to be deleted.

        Returns:
            bool: True if the task was deleted successfully, False otherwise.
        """
        with Session(self._engine) as session:
            task = session.query(Task).filter(Task.id == task_id).first()

            if task is not None:
                session.delete(task)
                session.commit()
                return True

            return False
