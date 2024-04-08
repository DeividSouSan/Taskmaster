from flask import Blueprint, render_template
from flask_login import login_required

from src.forms.login_form import LoginForm
from src.forms.register_form import RegisterForm
from src.forms.task_form import TaskForm

view = Blueprint("view", __name__)


@view.route("/")
def index():
    return render_template("index.html", title="Home - Taskmaster")


@view.route("/login", methods=["GET"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login - Taskmaster", form=form)


@view.route("/register", methods=["GET"])
def register():
    form = RegisterForm()
    return render_template("register.html", title="Cadastro - Taskmaster", form=form)


@view.route("/board", methods=["GET"])
@login_required
def board():
    form = TaskForm()

    return render_template(
        "board.html", title="Quadro de Tarefas - Taskmaster", form=form
    )
