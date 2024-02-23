from flask import Blueprint, redirect, request, render_template, url_for
from flask_login import current_user, login_required, logout_user
from flask import current_app
from ..forms.register_form import RegisterForm
from ..forms.login_form import LoginForm
from ..use_cases.user.register_user_use_case import RegisterUserUseCase
from ..use_cases.user.login_user_use_case import LoginUserUseCase
from ..repositories.user_repository import UserRepository


bp = Blueprint("website", __name__)


@bp.route("/")
def index():
    return render_template("index.html", title="Taskmaster - Index")


@bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    error = None

    if request.method == "POST":
        if form.validate_on_submit():

            repository = UserRepository()

            use_case = RegisterUserUseCase(form, repository)
            success = use_case.attempt_registration()

            if success:
                return redirect(url_for("website.register"))

            error = error.message

    return render_template("register.html", title="Taskmaster - Cadastro", form=form, error=error)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if request.method == "POST":

            repository = UserRepository()
            use_case = LoginUserUseCase(form, repository)
            result = use_case.attempt_login_user()

            if result:
                return redirect(url_for("website.board"))

    return render_template("login.html", title="Taskmaster - Login", form=form)


@bp.route("/board")
@login_required
def board():
    print("entramos na rota")

    return render_template("board.html", title="board", user=current_user)
