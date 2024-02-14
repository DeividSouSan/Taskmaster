from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository():

    def __init__(self, engine):
        self.engine = engine

    def add_user(self, user):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()

    def exists_user_with_username(self, username):
        with Session(self.engine) as session:
            result = session.query(User).filter(
                User.username == username).first()

            print("resultado user", result)
            return bool(result)

    def exists_user_with_email(self, email):
        with Session(self.engine) as session:
            result = session.query(User).filter(User.email == email).first()
            print("resultado email", result)
            return bool(result)

    def get_user_password_hash(self, email):
        with Session(self.engine) as session:
            result = session.query(User).filter(User.email == email).first()
            print("User:", result.password_hash)
