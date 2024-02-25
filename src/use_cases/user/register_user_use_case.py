"""
This module implements the Register User use case.
"""

from datetime import datetime
from ...repositories.user_repository import IUserRepository
from ...models.user import User
from ...utils.password_hasher import PassowordHash
from ...forms.register_form import IRegisterForm


class RegisterUserUseCase():
    """
    Use case class for registering a new user.

    This class handles the logic for registering a new user in the system. It
    checks if the provided username and email are already taken, hashes the password,
    and creates a new User object with the provided information. The user is then
    added to the repository.

    Attributes
        repository (UserRepository): The repository for accessing user data.
        form (Form): The form containing the user registration data.
        error (dict): An error object containing information about any validation errors
        encountered during registration.

    Methods:
        execute(): Executes the registration use case logic.
    """

    def __init__(self, form: IRegisterForm, repository: IUserRepository):
        self.__repository = repository
        self.__form = form
        self.error = None

    def attempt_registration(self) -> bool:
        """
        Executes the registration use case logic.

        This method uses the form data to register a new user. It extracts the username and email
        from the form data and performs the necessary operations to register the user.

        Returns:
            False - If the username or email is already taken.
            True - If the user is successfully registered.
        """

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
        """
        Checks if a field is already taken.

        This method checks if a field is already taken by querying the repository for
        a user with the given field value.

        Args:
            field (str): The field to check.
            value (str): The value to check.

        Returns:
            bool: True if the field is already taken, False otherwise.
        """
        field_is_taken = self.__repository.exists_user_with_field(field, value)
        return field_is_taken
