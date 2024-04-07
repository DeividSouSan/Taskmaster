from datetime import datetime

from flask import flash

from ...forms.register_form import RegisterForm
from ...models.user import User
from ...repositories.user_repository import UserRepository
from ...utils.check_form_fields import CheckFormFields
from ...utils.password_hasher import PasswordHash


class RegisterUserUseCase:
    form: RegisterForm
    repository: UserRepository
    pwd_hasher: PasswordHash

    def __init__(
        self, form: RegisterForm, repository: UserRepository, pwd_hahser: PasswordHash
    ):
        self.__form = form
        self.__repository = repository
        self.__pwd_hasher = pwd_hahser

    def attempt_registration(self) -> bool:

        user = self.create_user()

        if CheckFormFields.is_field_with_whitespaces(self.__form):
            self.notify_field_with_whitespaces()
            return False

        unique_fields = [
            {"name": "username", "value": user.username},
            {"name": "email", "value": user.email},
        ]

        if field := CheckFormFields.is_field_taken(
            self, unique_fields, self.__repository
        ):
            notify = {
                "username": self.notify_username_alredy_used,
                "email": self.notify_email_already_used,
            }

            notify[field]()

            return False

        self.__repository.add_user(user)
        self.notify_successful_register()
        return True

    def create_user(self) -> User:
        return User(
            username=self.__form.username.data,
            password_hash=self.__pwd_hasher.hash_password(self.__form.password.data),
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

    def notify_field_with_whitespaces(self) -> None:
        flash("Os campos não podem começar ou terminar com espaços", "error")
