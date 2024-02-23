from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..models.task import Task
from ..database.db import db


class User(db.Model):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    fullname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    registration: Mapped[datetime]
    tasks: Mapped[list["Task"]] = relationship()
