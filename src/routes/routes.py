from flask import Blueprint, redirect, request, render_template, url_for
from src.forms.register import RegisterForm
from src.forms.login import LoginForm
from src.use_cases.user.register_user_use_case import RegisterUserUseCase
from src.use_cases.user.login_user_use_case import LoginUserUseCase


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

            useCase = RegisterUserUseCase(form)
            result = useCase.execute()

            if result == True:
                redirect(url_for("website.register"))

            error = useCase.error

    return render_template("register.html", title="Taskmaster - Cadastro", form=form, error=error)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    print("entramos na rota")

    if form.validate_on_submit():
        if request.method == "POST":
            print("formulário válido")
            useCase = LoginUserUseCase(form)
            result = useCase.execute()
            print("Já executou o caso de uso")

    return render_template("login.html", title="Taskmaster - Login", form=form)

# Nessa rota o usuário já precisa estar autenticado


@bp.route("/board")
def board():
    return render_template("board.html", title="board")
