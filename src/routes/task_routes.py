from flask import Blueprint, Response, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from src import htmx
from src.forms.task_form import TaskForm
from src.repositories.task_repository import TaskRepository
from src.use_cases.tasks.add_task_use_case import AddTaskUseCase
from src.use_cases.tasks.delete_task_use_case import MoveTaskToTrashUseCase
from src.use_cases.tasks.get_tasks_use_case import GetTasksUseCase
from src.models.task import TaskStatus

task = Blueprint("task", __name__)


def redirectResponse(route: str):
    response = Response()
    response.headers["hx-redirect"] = url_for(route)
    return response


@task.route("/get-tasks", methods=["GET"])
@login_required
def get():
    repository = TaskRepository()

    use_case = GetTasksUseCase(current_user.id, repository)

    filter_option = request.args.get('filter', 'normal')

    get_tasks_with_filter = {
        "normal": use_case.get_active_tasks(),
        "deleted": use_case.get_deleted_tasks()
    }

    tasks = get_tasks_with_filter[filter_option]

    return render_template(
        "partials/task-container.html",
        tasks=tasks,
        TaskStatus=TaskStatus,
        filter=filter_option)


@task.route("/search-tasks", methods=["GET"])
def search():
    text = request.args.get("text-to-search")
    print("Texto para procurar:", text)
    repository = TaskRepository()

    use_case = GetTasksUseCase(current_user.id, repository)
    tasks = use_case.get_tasks_like(text)

    return render_template(
        "partials/task-container.html",
        tasks=tasks,
        TaskStatus=TaskStatus)


@task.route("/add-task", methods=["POST"])
@login_required
def add():
    form = TaskForm()
    repository = TaskRepository()

    if form.validate_on_submit():
        use_case = AddTaskUseCase(current_user.id, form, repository)
        use_case.add()

    return redirect(url_for("view.board"))


@task.route("/trash-task/<task_id>", methods=["PATCH"])
@login_required
def trash(task_id):
    repository = TaskRepository()

    use_case = MoveTaskToTrashUseCase(task_id, repository)
    use_case.move_task_to_trash()

    if htmx:
        return redirectResponse("view.board")

    return redirect(url_for("view.board"))


@task.route("/delete-task/<id>", methods=["POST"])
@login_required
def delete(id):
    form = TaskForm()
    repository = TaskRepository()

    if form.validate_on_submit():
        use_case = AddTaskUseCase(current_user.id, form, repository)
        use_case.add()

    return redirect(url_for("view.board"))
