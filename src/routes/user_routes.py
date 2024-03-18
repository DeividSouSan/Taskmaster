from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from src import htmx
from src.forms.task_form import TaskForm
from src.repositories.task_repository import TaskRepository
from src.use_cases.tasks.add_task_use_case import AddTaskUseCase
from src.use_cases.tasks.delete_task_use_case import DeleteTaskUseCase
from src.use_cases.tasks.get_tasks_use_case import GetTasksUseCase
from src.models.task import TaskStatus

user = Blueprint("user", __name__)


@user.route("/board", methods=["GET"])
def board():
    form = TaskForm()
    repository = TaskRepository()

    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))

    use_case = GetTasksUseCase(current_user.id, repository)

    filter_option = request.args.get('filter', 'normal')

    current_filter = {
        "normal": use_case.get_active_tasks(),
        "deleted": use_case.get_deleted_tasks()
    }

    tasks = current_filter[filter_option]

    if htmx:
        return render_template("partials/task-container.html", tasks=tasks, TaskStatus=TaskStatus, filter=filter_option)

    return render_template(
        "board.html",
        title="Quadro de Tarefas - Taskmaster",
        user=current_user,
        tasks=tasks,
        TaskStatus=TaskStatus,
        form=form,
        filter=filter_option)


@user.route("/add_task", methods=["POST"])
@login_required
def add_task():
    form = TaskForm()
    repository = TaskRepository()

    use_case = AddTaskUseCase(current_user.id, form, repository)
    use_case.add_task()

    return redirect(url_for("user.board"))


@user.route("/delete_task/<task_id>", methods=["GET", "DELETE"])
@login_required
def delete_task(task_id):
    repository = TaskRepository()

    use_case = DeleteTaskUseCase(task_id, repository)
    use_case.delete_task()

    return redirect(url_for("user.board"), code=303)
