from flask import flash
from flask_login import login_user

from src.utils.user_login_notifier import UserLoginNotifier

from ...forms.login_form import LoginForm
from ...repositories.user_repository import UserRepository
from ...utils.check_form_fields import CheckFormFields
from ...utils.password_hasher import PasswordHash


class LoginUserUseCase:

    def __init__(
        self, form: LoginForm, repository: UserRepository, pwd_hasher: PasswordHash, check_form_fields: CheckFormFields, notifier: UserLoginNotifier
    ):
        self.__repository = repository
        self.__form = form
        self.__pwd_hasher = pwd_hasher
        self.__check_form_fields = check_form_fields
        self.__notifier = notifier

    def attempt_login_user(self) -> bool:

        # Checa se os dados possuem espaços em branco
        if self.__check_form_fields.is_field_with_whitespaces(self.__form):
            self.__notifier.notify_field_with_whitespaces()
            return False

        username = self.__form.username.data
        password = self.__form.password.data

        # Checa se o usuário existe e se a senha está correta
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
                self.__notifier.notify_wrong_password()

            return pwd_is_correct

        self.__notifier.notify_user_not_found()
        return False

    
