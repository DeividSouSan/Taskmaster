from flask import Blueprint, Response, redirect, session, url_for
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
from src.utils.check_form_fields import FieldWhitespaceChecker
from src.utils.password_hasher import PasswordHash
from src.utils.user_creator import UserCreator
from src.utils.user_login_notifier import UserLoginNotifier
from src.utils.user_registration_notifier import UserRegistrationNotifier

auth = Blueprint("auth", __name__)

# Utilities functions


def redirect_response(route: str):
    response = Response()
    response.headers["hx-redirect"] = url_for(route)
    return response


# Login manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# Routes


@auth.route("/register", methods=["POST"])
def register():
    form = RegisterForm()
    repository = UserRepository()
    pwd_hasher = PasswordHash()
    whitespace_checker = FieldWhitespaceChecker()
    notifier = UserRegistrationNotifier()

    if form.validate_on_submit():

        if whitespace_checker.is_field_with_whitespaces(form):
            notifier.notify_field_with_whitespaces()
            return redirect(url_for("view.register"))

        user_creator = UserCreator(pwd_hasher)
        user = user_creator.create(form)

        use_case = RegisterUserUseCase(repository, notifier)
        result = use_case.attempt_registration(user)

        if result:
            return redirect(url_for("view.login"))

    session["form_data"] = form.data
    return redirect(url_for("view.register"))


@auth.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    repository = UserRepository()
    pwd_hasher = PasswordHash()
    whitespace_checker = FieldWhitespaceChecker()
    notifier = UserLoginNotifier()

    if form.validate_on_submit():

        if whitespace_checker.is_field_with_whitespaces(form):
            notifier.notify_field_with_whitespaces()
            return redirect(url_for("view.login"))

        user_data = {
            "username": form.data["username"],
            "password": form.data["password"],
        }

        use_case = LoginUserUseCase(user_data, repository, pwd_hasher, notifier)
        result = use_case.attempt_login_user()

        if result:
            return redirect(url_for("view.board"))

    session["form_data"] = form.data
    return redirect(url_for("view.login"))


@auth.route("/logout", methods=["GET"])
@login_required
def logout():

    use_case = LogoutUserUseCase()
    use_case.execute_logout()

    if htmx:
        return redirect_response("auth.login")

    return redirect(url_for("auth.login"))


@auth.route("/delete_account/<user_id>", methods=["DELETE"])
@login_required
def delete_account(user_id):
    """
    Deletes user account.

    Deletes the user account from the database trough the DeleteAccountUseCase and redirects to the login page.

    Attributes:
        user_id: The id of the user to be deleted.

    Returns:
        Response: Redirects to the login page.
    """
    # TODO: needs to delete the tasks too
    repository = UserRepository()

    use_case = DeleteAccountUseCase(user_id, repository)
    use_case.execute()

    return redirect_response("view.login")
