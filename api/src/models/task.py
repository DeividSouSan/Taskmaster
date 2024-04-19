import enum
from datetime import datetime

from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src import db


class TaskStatus(enum.Enum):
    """
    Enumerator for handling the status of the task.

    Attributes:
        NOT_STARTED: The task has not been started.
        DOING: The task is currently being done.
        FINISHED: The task has been finished.
    """

    NOT_STARTED: int = 0
    DOING: int = 1
    FINISHED: int = 2


class Task(db.Model):
    """
    This class is a model for the Tasks table in the database.

    Through this class, we can interact with the Tasks table in the database. It has the fields of the table as attributes.

    Attributes:
        id: The primary key of the table.
        user_id: The foreign key of the Users table.
        task_title: The title of the task.
        task_description: The description of the task.
        due_date: The due date of the task.
        status: The status of the task (0: Not Started, 1: Doing, 2: Finished)
    """

    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(200))
    due_date: Mapped[datetime] = mapped_column(nullable=True)
    status: Mapped[int]
