from flask import flash
from flask_login import login_user

from ...forms.login_form import LoginForm
from ...repositories.user_repository import UserRepository
from ...utils.password_hasher import PasswordHash


class LoginUserUseCase:

    def __init__(
        self, form: LoginForm, repository: UserRepository, pwd_hasher: PasswordHash
    ):
        self.__repository = repository
        self.__form = form
        self.__pwd_hasher = pwd_hasher

    def attempt_login_user(self) -> bool:
        username = self.__form.username.data
        password = self.__form.password.data

        valid_credentials = self.verify_credentials(username, password)

        if valid_credentials:
            user = self.__repository.get_user_by_username(username)
            # Essa é a única dependência desse código
            result = login_user(user)

            if result:
                return True

        return False

    def verify_credentials(self, username: str, password: str) -> bool:
        user_exists = self.__repository.exists_user_with_field("username", username)

        if user_exists:
            database_password = self.__repository.get_user_password_by_username(
                username
            )

            pwd_is_correct = self.__pwd_hasher.check_password(
                password, database_password
            )

            if not pwd_is_correct:
                self.notify_wrong_password()

            return pwd_is_correct

        self.notify_user_not_found()
        return False

    def notify_user_not_found(self) -> None:
        flash("Usuário não encontrado", "error")

    def notify_wrong_password(self) -> None:
        flash("Senha incorreta", "error")
