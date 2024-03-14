from datetime import datetime
from flask import flash

from ...repositories.user_repository import UserRepository
from ...models.user import User
from ...utils.password_hasher import PasswordHash
from ...forms.register_form import RegisterForm


class RegisterUserUseCase():
    def __init__(self, form: RegisterForm, repository: UserRepository, pwd_hahser: PasswordHash):
        self.__form = form
        self.__repository = repository
        self.__pwd_hasher = pwd_hahser

    def attempt_registration(self) -> bool:

        user = self.create_user()

        if self.is_field_taken("username", user.username):
            flash("Nome de usuário já foi utilizado", "error")
            return False

        if self.is_field_taken("email", user.email):
            flash("Email já foi utlizado", "error")
            return False

        self.__repository.add_user(user)
        flash("Usuário cadastrado com sucesso", "success")
        return True

    def is_field_taken(self, field, value):
        field_is_taken = self.__repository.exists_user_with_field(field, value)
        return field_is_taken

    def create_user(self):
        return User(
            username=self.__form.username.data,
            password_hash=self.__pwd_hasher.hash_password(self.__form.password.data),
            fullname=self.__form.fullname.data,
            email=self.__form.email.data,
            registration=datetime.now(),
        )
