class UserRegistrationNotifier:
    def notify_successful_register(self) -> None:
        flash("Usuário cadastrado com sucesso", "success")

    def notify_email_already_used(self) -> None:
        flash("Email já foi utlizado", "error")

    def notify_username_alredy_used(self) -> None:
        flash("Nome de usuário já foi utilizado", "error")

    def notify_field_with_whitespaces(self) -> None:
        flash("Os campos não podem começar ou terminar com espaços", "error")