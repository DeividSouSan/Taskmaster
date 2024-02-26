from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user

from src.forms.task_form import TaskForm
from src.repositories.task_repository import TaskRepository
from src.use_cases.tasks.add_task_use_case import AddTaskUseCase

user = Blueprint("user", __name__)

tasks = []


@user.route("/board", methods=["GET", "POST"])
def board():
    form = TaskForm()

    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        repository = TaskRepository()

        use_case = AddTaskUseCase(current_user.id, form, repository)

        use_case.add_task()

    return render_template(
        "user_specific/board.html",
        title="board",
        user=current_user,
        tasks=tasks,
        form=form)
