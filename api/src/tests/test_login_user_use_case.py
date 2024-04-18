import unittest
from unittest.mock import Mock, patch

from flask import current_app

from src import create_app
from src.use_cases.user.login_user_use_case import LoginUserUseCase


class TestLoginUserUseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.form_mock = Mock()
        self.repository_mock = Mock()
        self.pwd_hash_mock = Mock()
        self.usecase = LoginUserUseCase(
            self.form_mock, self.repository_mock, self.pwd_hash_mock
        )

    def test_attempt_login_user_with_valid_credentials(self):

        # Dados do formulário enviado
        self.form_mock.username.data = "username"
        self.form_mock.password.data = "password"

        # Existe usuário no banco de dados
        self.repository_mock.exists_user_with_field.return_value = True
        self.repository_mock.get_user_password_by_username.return_value = (
            "hashed_password"
        )
        self.pwd_hash_mock.check_password.return_value = True

        # Simula a aplicação e um contexto de requisição
        with self.app.app_context():
            with self.app.test_request_context():
                result = self.usecase.attempt_login_user()

        self.assertTrue(result)
        self.repository_mock.get_user_by_username.assert_called_once_with("username")
        self.repository_mock.exists_user_with_field.assert_called_once_with(
            "username", "username"
        )
        self.repository_mock.get_user_password_by_username.assert_called_once_with(
            "username"
        )
        self.pwd_hash_mock.check_password.assert_called_once_with(
            "password", "hashed_password"
        )

    def test_attempt_login_user_not_registered_(self):

        # Dados do formulário enviado
        self.form_mock.username.data = "username"
        self.form_mock.password.data = "password"

        # Não existe o  usuário no banco de dados
        self.repository_mock.exists_user_with_field.return_value = False

        # Simula a aplicação e um contexto de requisição
        with self.app.app_context():
            with self.app.test_request_context():
                result = self.usecase.attempt_login_user()

        self.assertFalse(result)
        self.repository_mock.exists_user_with_field.assert_called_once_with(
            "username", "username"
        )
