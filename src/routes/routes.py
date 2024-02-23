from flask import Blueprint, redirect, request, render_template, url_for
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

    print("entramos na rota")

    if form.validate_on_submit():
        if request.method == "POST":
            use_case = LoginUserUseCase(form)
            result = use_case.execute()

    return render_template("login.html", title="Taskmaster - Login", form=form)

# Nessa rota o usuário já precisa estar autenticado


@bp.route("/board")
def board():
    return render_template("board.html", title="board")
