import enum
from datetime import datetime
from sqlalchemy import ForeignKey, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from src import db

class TaskStatus(enum.Enum):
    NOT_STARTED: int = 0
    DOING: int = 1
    FINISHED: int = 2


class Task(db.Model):
    """
    Attr:
    id
    user_id
    task_title
    task_description
    due_date
    status
    """
    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(200))
    due_date: Mapped[datetime] = mapped_column(nullable=True)
    status: Mapped[int]
