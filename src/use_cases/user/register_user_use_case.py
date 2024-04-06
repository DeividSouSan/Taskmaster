from datetime import datetime

from flask import flash

from ...forms.register_form import RegisterForm
from ...models.user import User
from ...repositories.user_repository import UserRepository
from ...utils.password_hasher import PasswordHash


class RegisterUserUseCase:
    def __init__(
        self, form: RegisterForm, repository: UserRepository, pwd_hahser: PasswordHash
    ):
        self.__form = form
        self.__repository = repository
        self.__pwd_hasher = pwd_hahser

    def attempt_registration(self) -> bool:

        if self.is_field_with_whitespaces():
            self.notify_field_with_whitespaces()
            return False

        user = self.create_user()

        if self.is_field_taken("username", user.username):
            self.notify_username_alredy_used()
            return False

        if self.is_field_taken("email", user.email):
            self.notify_email_already_used()
            return False

        self.__repository.add_user(user)
        self.notify_successful_register()
        return True

    def is_field_taken(self, field: str, value: any) -> bool:
        field_is_taken = self.__repository.exists_user_with_field(field, value)
        return field_is_taken

    def is_field_with_whitespaces(self) -> bool:
        for field in self.__form:
            if field.data.startswith(" ") or field.data.endswith(" "):
                return True
        return False

    def create_user(self) -> User:
        return User(
            username=self.__form.username.data,
            password_hash=self.__pwd_hasher.hash_password(
                self.__form.password.data),
            fullname=self.__form.fullname.data,
            email=self.__form.email.data,
            registration=datetime.now(),
        )

    def notify_successful_register(self) -> None:
        flash("Usuário cadastrado com sucesso", "success")

    def notify_email_already_used(self) -> None:
        flash("Email já foi utlizado", "error")

    def notify_username_alredy_used(self) -> None:
        flash("Nome de usuário já foi utilizado", "error")

    
