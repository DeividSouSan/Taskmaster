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

    def exists_user_with_field(self, field, given_value):
        with Session(self.engine) as session:
            user_attribute = getattr(User, field)
            result = session.query(User).filter(
                user_attribute == given_value).first()
            return bool(result)

    def get_user_password_hash(self, email):
        with Session(self.engine) as session:
            result = session.query(User).filter(User.email == email).first()
            print("User:", result.password_hash)
