import unittest
from datetime import datetime
from unittest.mock import Mock

from flask import current_app

from src import create_app
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.use_cases.user.register_user_use_case import RegisterUserUseCase
from src.utils.user_registration_notifier import UserRegistrationNotifier


class TestRegisterUserUseCase(unittest.TestCase):

    def setUp(self):
        # Configuring the application
        self.app = create_app("TestingConfig")
        self.app.testing = True

        self.client = self.app.test_client()

        with self.app.app_context():
            repository = UserRepository()
            repository.delete_table()

        # Mocks
        self.notifier = Mock()

    def tearDown(self):
        # Deleting the Test Table
        with self.app.app_context():
            repository = UserRepository()
            repository.delete_table()

    def test_register_user(self):
        with self.app.app_context():
            repository = UserRepository()

        use_case = RegisterUserUseCase(repository, self.notifier)

        user = User(
            username="test_user",
            password_hash="test_password",
            fullname="Test User",
            email="test@email.com",
            registration=datetime.now(),
        )

        attempt_result = use_case.attempt_registration(user)
        self.assertEqual(
            attempt_result, True, "User instance  data is already in the database."
        )

        user_in_db = repository.get_user_by_username("test_user")
        self.assertIsInstance(user_in_db, User, "User was not added to the database")

    def test_register_the_same_user(self):
        # Criando o usuário
        user = User(
            username="test_user",
            password_hash="test_password",
            fullname="Test User",
            email="test@email.com",
            registration=datetime.now(),
        )

        # Criando a instância do repositório
        with self.app.app_context():
            repository = UserRepository()

        # Criando a instância do caso de uso
        use_case = RegisterUserUseCase(repository, self.notifier)

        # Cadastrando um usuário
        result = use_case.attempt_registration(user)
        self.assertEqual(result, True, "User data already in use")

        # Verificando se o usuário foi cadastrado
        user = repository.get_user_by_username("test_user")
        self.assertIsInstance(user, User, "User was not created")

        # Tentando cadastrar o mesmo usuário
        result = use_case.attempt_registration(user)
        self.assertEqual(result, False, "User data was not in use")

    def test_username_already_used(self):
        # Criando o usuário
        user = User(
            username="test_user",
            password_hash="test_password",
            fullname="Test User",
            email="test@email.com",
            registration=datetime.now(),
        )

        # Criando a instância do repositório
        with self.app.app_context():
            repository = UserRepository()

        # Criando a instância do caso de uso
        use_case = RegisterUserUseCase(repository, self.notifier)

        # Cadastrando um usuário
        result = use_case.attempt_registration(user)
        self.assertEqual(result, True, "User data already in use")

        # Verificando se o usuário foi cadastrado
        user = repository.get_user_by_username("test_user")
        self.assertIsInstance(user, User, "User was not created")

        # Criando um usuário com o mesmo nome de usuário e email diferente
        user = User(
            username="test_user",
            password_hash="test_password",
            fullname="Test User",
            email="different_test@email.com",
            registration=datetime.now(),
        )

        # Verificando se o nome de usuário utilizado no cadastro já foi utilizado
        result_check_field_unique = use_case._RegisterUserUseCase__check_unique_fields(
            user
        )
        self.assertEqual(
            result_check_field_unique, "username", "Username was not being used"
        )

        # Criando o usuário com o mesmo nome de usuário
        result = use_case.attempt_registration(user)
        self.assertEqual(result, False, "User data was not in use")

    def test_email_already_used(self):

        # Criando o usuário
        user = User(
            username="test_user",
            password_hash="test_password",
            fullname="Test User",
            email="test@email.com",
            registration=datetime.now(),
        )

        # Criando a instância do repositório
        with self.app.app_context():
            repository = UserRepository()

        # Criando a instância do caso de uso
        use_case = RegisterUserUseCase(repository, self.notifier)

        # Cadastrando um usuário
        result = use_case.attempt_registration(user)
        self.assertEqual(result, True, "User data already in use")

        # Verificando se o usuário foi cadastrado
        user = repository.get_user_by_username("test_user")
        self.assertIsInstance(user, User, "User was not created")

        # Criando um usuário com o mesmo email
        user = User(
            username="different_test_user",
            password_hash="test_password",
            fullname="Test User",
            email="test@email.com",
            registration=datetime.now(),
        )

        # Verificando se o email utilizado no cadastro já foi utilizado
        result_check_unique_field = use_case._RegisterUserUseCase__check_unique_fields(
            user
        )
        self.assertEqual(result_check_unique_field, "email", "Email was not being used")

    def test_register_new_user(self):

        user = User(
            username="new_user",
            password_hash="new_password",
            fullname="New Test User",
            email="new_test@email.com",
            registration=datetime.now(),
        )

        with self.app.app_context():
            repository = UserRepository()

        use_case = RegisterUserUseCase(repository, self.notifier)
        result = use_case.attempt_registration(user)

        self.assertEqual(result, True, "User data already in use")
