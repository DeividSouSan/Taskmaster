from flask import flash
from flask_login import login_user

from src.utils.user_login_notifier import UserLoginNotifier

from ...forms.login_form import LoginForm
from ...repositories.user_repository import UserRepository
from ...utils.check_form_fields import FieldWhitespaceChecker
from ...utils.password_hasher import PasswordHash


class LoginUserUseCase:
    user: dict[str, str]
    repository: UserRepository
    pwd_hasher: PasswordHash
    notifier: UserLoginNotifier

    def __init__(
        self,
        user: dict[str, str],
        repository: UserRepository,
        pwd_hasher: PasswordHash,
        notifier: UserLoginNotifier,
    ):
        self.__repository = repository
        self.__user = user
        self.__pwd_hasher = pwd_hasher
        self.__notifier = notifier

    def attempt_login_user(self) -> bool:

        username = self.__user["username"]
        password = self.__user["password"]

        if self.__is_credentials_valid(username, password):
            user = self.__repository.get_user_by_username(username)
            login_success = login_user(user)

            return True if login_success else False

    def __is_credentials_valid(self, username: str, password: str) -> bool:
        if self.__repository.exists_user_with_field("username", username):
            database_pwd = self.__repository.get_user_password_by_username(username)

            pwd_is_correct = self.__pwd_hasher.check_password(password, database_pwd)

            if not pwd_is_correct:
                self.__notifier.notify_wrong_password()

            return pwd_is_correct

        self.__notifier.notify_user_not_found()
        return False
