from flask import flash


class UserLoginNotifier:
    def notify_user_not_found(self) -> None:
        flash("Usuário não encontrado", "error")

    def notify_wrong_password(self) -> None:
        flash("Senha incorreta", "error")

    def notify_field_with_whitespaces(self) -> None:
        flash("Os campos não podem começar ou terminar com espaços", "error")
