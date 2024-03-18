from flask import Blueprint, request, redirect, url_for, render_template, Response
from flask_login import login_required
from src import login_manager, htmx
from src.forms.login_form import LoginForm
from src.forms.register_form import RegisterForm
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.use_cases.user.delete_account_use_case import DeleteAccountUseCase
from src.use_cases.user.logout_user_use_case import LogoutUserUseCase
from src.use_cases.user.login_user_use_case import LoginUserUseCase
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


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    repository = UserRepository()
    pwd_hasher = PasswordHash()

    if request.method == "POST":
        if form.validate_on_submit():
            
            use_case = RegisterUserUseCase(form, repository, pwd_hasher)
            success = use_case.attempt_registration()

            if success:
                return redirect(url_for("auth.login"))

    return render_template(
        "register.html",
        title="Cadastro - Taskmaster",
        form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    repository = UserRepository()
    pwd_hasher = PasswordHash()

    if request.method == "POST":
        if form.validate_on_submit():

            use_case = LoginUserUseCase(form, repository, pwd_hasher)
            result = use_case.attempt_login_user()

            if result:
                return redirect(url_for("user.board"))

    return render_template(
        "login.html",
        title="Login - Taskmaster",
        form=form)


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
