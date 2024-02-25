from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

from src.forms.task_form import TaskForm

user = Blueprint("user", __name__)

tasks = []


@user.route("/board")
@login_required
def board():
    form = TaskForm()

    if not current_user.is_authenticated:
        return redirect(url_for("website.login"))

    return render_template(
        "user_specific/board.html",
        title="board",
        user=current_user,
        tasks=tasks,
        form=form)
