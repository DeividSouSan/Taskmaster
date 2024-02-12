from sqlalchemy.orm import Session


class UserRepository():

    def __init__(self, engine):
        self.engine = engine

    def add_user(self, user):
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
