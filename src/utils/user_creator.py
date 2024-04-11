from datetime import datetime

from src.forms.register_form import RegisterForm
from src.models.user import User
from src.utils.password_hasher import PasswordHash


class UserCreator:
    def __init__(self, pwd_hasher: PasswordHash):
        self.__pwd_hasher = pwd_hasher

    def create(self, form: RegisterForm) -> User:
        return User(
            username=form.username.data,
            password_hash=self.__pwd_hasher.hash_password(form.password.data),
            fullname=form.fullname.data,
            email=form.email.data,
            registration=datetime.now(),
        )
