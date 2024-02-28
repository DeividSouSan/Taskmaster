from datetime import datetime
from flask import flash

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

        user = self.create_user()

        if self.is_field_taken("username", user.username):
            flash("Nome de usuário já foi utilizado")
            return False

        if self.is_field_taken("email", user.email):
            flash("Email já foi utlizado")
            return False

        self.__repository.add_user(user)
        return True

    def is_field_taken(self, field, value):
        field_is_taken = self.__repository.exists_user_with_field(field, value)
        return field_is_taken

    def create_user(self):
        return User(
            username=self.__form.username.data,
            password_hash=PassowordHash().hash_password(self.__form.password.data),
            fullname=self.__form.fullname.data,
            email=self.__form.email.data,
            registration=datetime.now(),
        )
