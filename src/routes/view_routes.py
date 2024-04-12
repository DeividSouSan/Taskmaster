from flask import Blueprint, render_template, redirect, session, url_for, current_app, request
from flask_login import login_required, current_user
from src.forms.login_form import LoginForm
from src.forms.register_form import RegisterForm
from src.forms.task_form import TaskForm

view = Blueprint("view", __name__)


@view.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for("view.board"))

    return render_template("index.html", title="Home - Taskmaster")


@view.route("/register", methods=["GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("view.board"))

    form = RegisterForm()
    if "form_data" in session:
        form.process(data=session["form_data"])
        session.pop("form_data")

    return render_template("register.html", title="Cadastro - Taskmaster", form=form)


@view.route("/login", methods=["GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("view.board"))

    form = LoginForm()
    if "form_data" in session:
        form.process(data=session["form_data"])
        session.pop("form_data")

    return render_template("login.html", title="Login - Taskmaster", form=form)


@view.route("/board", methods=["GET"])
@login_required
def board():
    form = TaskForm()

    return render_template(
        "board.html", title="Quadro de Tarefas - Taskmaster", form=form
    )
