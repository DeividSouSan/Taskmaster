"""
This module implements the Register User use case.
"""

from datetime import datetime
from ...repositories.user_repository import IUserRepository
from ...models.user import User
from ...utils.password_hasher import PassowordHash
from ...forms.register_form import IRegisterForm


class RegisterUserUseCase():
    def __init__(self, form: IRegisterForm, repository: IUserRepository):
        self.__repository = repository
        self.__form = form
        self.error = None

    def attempt_registration(self) -> bool:
        username: str = self.__form.username.data
        email: str = self.__form.email.data
        password: str = self.__form.password.data
        fullname: str = self.__form.fullname.data
        registration_date: datetime = datetime.now()

        if self.is_field_taken("username", username):
            self.error = {"type": "username", "message": "Username already taken"}
            return False

        if self.is_field_taken("email", email):
            self.error = {"type": "email", "message": "Email already taken"}
            return False

        password_hash = PassowordHash().hash_password(password)

        user = User(
            username=username,
            password_hash=password_hash,
            fullname=fullname,
            email=email,
            registration=registration_date,
        )

        self.__repository.add_user(user)
        return True

    def is_field_taken(self, field, value):
        field_is_taken = self.__repository.exists_user_with_field(field, value)
        return field_is_taken
