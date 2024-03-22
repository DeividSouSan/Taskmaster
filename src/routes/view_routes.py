from flask import Blueprint, render_template
from src.forms.login_form import LoginForm

view = Blueprint("view", __name__)


@view.route("/")
def index():
    return render_template(
        "index.html", 
        title="Home - Taskmaster")


@view.route("/board", methods=["GET"])
def board():
    return render_template(
        "board.html",
        title="Quadro de Tarefas - Taskmaster")


@view.route("/login", methods=["GET"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)


@view.route("/register", methods=["GET"])
def register():
    return render_template("register.html")
