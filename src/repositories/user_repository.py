from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ..models.user import User


class UserRepository:

    def __init__(self):
        with current_app.app_context():
            DATABASE_URI = current_app.config['SQLALCHEMY_DATABASE_URI']

        self.engine = create_engine(DATABASE_URI)

    def add_user(self, user: User):
        with Session(self.engine) as session:
            try:
                session.add(user)
                session.commit()
                return True
            except:
                return False

    def get_user_password_by_username(self, username) -> str:
        with Session(self.engine) as session:
            user = session.query(User).filter(
                User.username == username).first()
            return user.password_hash

    def get_user_by_username(self, username) -> User:
        with Session(self.engine) as session:
            user = session.query(User).filter(
                User.username == username).first()
            return user

    def exists_user_with_field(self, field, given_value) -> bool:
        with Session(self.engine) as session:
            user_attribute = getattr(User, field)
            result = session.query(User).filter(
                user_attribute == given_value).first()
            return bool(result)

    def delete_user_by_id(self, user_id) -> bool:
        with Session(self.engine) as session:
            user = session.query(User).filter(User.id == user_id).first()

            try:
                session.delete(user)
                session.commit()

                return True
            except:

                return False
