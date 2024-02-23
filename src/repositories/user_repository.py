from typing import Protocol
from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ..models.user import User


class IUserRepository(Protocol):
    def add_user(self, user: User) -> None:
        ...

    def exists_user_with_field(self, field: str, given_value: str) -> bool:
        ...


class UserRepository:

    def __init__(self):
        with current_app.app_context():
            DATABASE_URI = current_app.config['DATABASE_URI']

        self.engine = create_engine(DATABASE_URI)

    def add_user(self, user):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()

    def exists_user_with_field(self, field, given_value):
        with Session(self.engine) as session:
            user_attribute = getattr(User, field)
            result = session.query(User).filter(
                user_attribute == given_value).first()
            return bool(result)
