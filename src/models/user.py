from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src import db


class User(db.Model, UserMixin):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    fullname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    registration: Mapped[datetime]
