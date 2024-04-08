from flask import flash

from src.repositories.user_repository import UserRepository


class DeleteAccountUseCase:

    def __init__(self, repository: UserRepository):
        self._repository = UserRepository()

    def delete_account(self, user_id):
        success = self._repository.delete_user_by_id(user_id)

        if success:
            flash("Conta deletada com sucesso", "error")
            return True
        else:
            flash("Delete todas as tarefas antes de deletar a conta", "error")
            return False
