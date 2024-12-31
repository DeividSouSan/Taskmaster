from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src import db


class User(db.Model, UserMixin):
    """
    Class for the Users table in the database.

    Through this class, we can interact with the Users table in the database. It has the fields of the table as attributes. It also inherits from UserMixin, which is a class from Flask-Login that has some methods that are necessary for the login system to work.

    Attributes:
        id: The primary key of the table.
        username: The username of the user.
        password_hash: The hashed password of the user.
        fullname: The full name of the user.
        email: The email of the user.
        registration: The registration date of the user.
    """

    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password_hash: Mapped[str] = mapped_column(String(100))
    fullname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    registration: Mapped[datetime]
