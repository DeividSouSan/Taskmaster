import enum
from datetime import datetime
from sqlalchemy import ForeignKey, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from src import db

class MyEnum(enum.Enum):
    NOT_STARTED = 0
    DOING = 1
    FINISHED = 2


class Task(db.Model):
    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    task_description: Mapped[str] = mapped_column(String(100))
    due_date: Mapped[datetime]
    status: Mapped[str] = mapped_column(Enum(MyEnum))
