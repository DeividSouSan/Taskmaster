from flask import Blueprint, Response, redirect, render_template, request, url_for
from flask_login import login_required

from src import htmx, login_manager
from src.forms.login_form import LoginForm
from src.forms.register_form import RegisterForm
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.use_cases.user.delete_account_use_case import DeleteAccountUseCase
from src.use_cases.user.login_user_use_case import LoginUserUseCase
from src.use_cases.user.logout_user_use_case import LogoutUserUseCase
from src.use_cases.user.register_user_use_case import RegisterUserUseCase
from src.utils.password_hasher import PasswordHash

auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def redirectResponse(route: str):
    response = Response()
    response.headers["hx-redirect"] = url_for(route)
    return response


@auth.route("/register", methods=["POST"])
def register():
    form = RegisterForm()
    repository = UserRepository()
    pwd_hasher = PasswordHash()

    if form.validate_on_submit():
        use_case = RegisterUserUseCase(form, repository, pwd_hasher)
        result = use_case.attempt_registration()

        if result:
            return redirect(url_for("view.login"))

    return redirect(url_for("view.register"))


@auth.route("/login", methods=["POST"])
def login():
    print("Ola")
    form = LoginForm()
    repository = UserRepository()
    pwd_hasher = PasswordHash()

    if form.validate_on_submit():
        use_case = LoginUserUseCase(form, repository, pwd_hasher)
        result = use_case.attempt_login_user()

        if result:
            return redirect(url_for("view.board"))

    return redirect(url_for("view.login"))


@auth.route("/logout", methods=["GET"])
@login_required
def logout():

    use_case = LogoutUserUseCase()
    use_case.execute_logout()

    if htmx:
        return redirectResponse("auth.login")

    return redirect(url_for("auth.login"))


@auth.route("/delete_account/<user_id>", methods=["GET", "DELETE"])
def delete_account(user_id):
    repository = UserRepository()

    use_case = DeleteAccountUseCase(repository)
    result = use_case.delete_account(user_id)

    if result:
        if htmx:
            return redirectResponse("auth.login")

        return redirect(url_for("auth.login"))

    if htmx:
        return redirectResponse("user.board")

    return redirect(url_for("user.board"))
