from flask import Blueprint, render_template

from src.forms.login_form import LoginForm
from src.forms.register_form import RegisterForm
from src.forms.task_form import TaskForm

form = Blueprint('form', __name__)


@form.route("/login-form", methods=['GET'])
def login_form():
    form = LoginForm()
    return render_template("partials/login-form.html", form=form)


@form.route("/register-form", methods=['GET'])
def register_form():
    form = RegisterForm()
    return render_template("partials/register-form.html", form=form)


@form.route("/add-task-form", methods=['GET'])
def add_task_form():
    form = TaskForm()
    return render_template("partials/add-task-form.html", form=form)


@form.route("/close-add-task-form", methods=['GET'])
def close_add_task_form():
    form = TaskForm()
    return render_template("partials/add-task-form.html", form=form)
