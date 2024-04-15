from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from ..models.user import User


class UserRepository:
    """
    Repository Class for the User model.

    Responsible for handling the database operations for the User model. It has methods for adding, getting, updating and deleting users from the database.

     The SQLALCHEMY_DATABASE_URI is obtained from the current_app.config, which is the configuration of the Flask application. This way, the repository can be used in the application context.

    If you want to change the database, you can change the SQLACLHEMY_DATABASE_URI in the configuration file of the application config.py.

    Attributes:
        _engine: The SQLAlchemy engine that connects to the database.
    """

    def __init__(self):
        with current_app.app_context():
            DATABASE_URI = current_app.config["SQLALCHEMY_DATABASE_URI"]

        self._engine = create_engine(DATABASE_URI)

    def add_user(self, user: User):
        """
        Adds a user to the database.

        Througn the session context manager, it adds the user to the database and commits the transaction.

        Args:
            user: The User object to be added to the database.

        Returns:
            bool: True if the user was added successfully, False otherwise.
        """
        with Session(self._engine) as session:
            # TODO: improve the exception handling, and return.
            try:
                session.add(user)
                session.commit()
                return True
            except:
                return False

    def get_user_password_by_username(self, username) -> str:

        with Session(self._engine) as session:
            user = session.query(User).filter(User.username == username).first()
            return user.password_hash

    def get_user_by_username(self, username) -> User:
        with Session(self._engine) as session:
            user = session.query(User).filter(User.username == username).first()
            return user

    def exists_user_with_field(self, field, given_value) -> bool:
        with Session(self._engine) as session:
            user_attribute = getattr(User, field)
            result = session.query(User).filter(user_attribute == given_value).first()
            return bool(result)

    def delete_user_by_id(self, user_id) -> None:
        with Session(self._engine) as session:
            user = session.query(User).filter(User.id == user_id).first()

            session.delete(user)
            session.commit()

    def delete_table(self):
        with Session(self._engine) as session:
            session.query(User).delete()
            session.commit()
            return True
