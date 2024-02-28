from flask import Blueprint, flash, request, redirect, url_for, render_template, Response
from flask_login import login_required, logout_user
from src import login_manager
from src.forms.login_form import LoginForm

from src.forms.register_form import RegisterForm
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.use_cases.user.login_user_use_case import LoginUserUseCase
from src.use_cases.user.register_user_use_case import RegisterUserUseCase

auth = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    error = None

    if request.method == "POST":
        if form.validate_on_submit():

            repository = UserRepository()

            use_case = RegisterUserUseCase(form, repository)
            success = use_case.attempt_registration()

            if success:
                return redirect(url_for("auth.login"))


    return render_template(
        "register.html",
        title="Taskmaster - Cadastro",
        form=form,
        error=error)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():

            repository = UserRepository()

            use_case = LoginUserUseCase(form, repository)
            result = use_case.attempt_login_user()

            if result:
                return redirect(url_for("user.board"))


    return render_template(
        "login.html",
        title="Taskmaster - Login",
        form=form)


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("Você foi deslogado com sucesso!", "alert")

    response = Response()
    response.headers["hx-redirect"] = url_for("auth.login")
    return response
