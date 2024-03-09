
from typing import Literal
from flask import flash
from flask_login import logout_user


class LogoutUserUseCase:
    def execute_logout(self) -> Literal[True]:
        logout_user()

        flash("Você foi deslogado com sucesso!", "alert")

        return True
