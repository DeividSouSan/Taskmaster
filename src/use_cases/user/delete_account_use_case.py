from flask import flash

from src.repositories.user_repository import UserRepository


class DeleteAccountUseCase:
    """
    Delete user account use case.

    This use case is responsible for deleting a user account from the database.

    Attributes:
        user_id: The id of the user to be deleted.
        repository: The repository that handles the database operations for the User model.

    Returns:
        None.

    """

    def __init__(self, user_id: int, repository: UserRepository):
        self._user_id = user_id
        self._repository = UserRepository()

    def execute(self) -> None:  # pylint: disable=missing-function-docstring
        try:
            self._repository.delete_user_by_id(self._user_id)
            flash("Conta deletada com sucesso", "error")
        except Exception as e:
            print(e)
            flash("Delete todas as tarefas antes de deletar a conta", "error")
