from flask import (
    Blueprint,
    Response,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user, login_required
from src.forms.task_form import TaskForm
from src.models.task import TaskStatus
from src.repositories.task_repository import TaskRepository
from src.use_cases.tasks.add_task_use_case import AddTaskUseCase
from src.use_cases.tasks.delete_task_use_case import DeleteTaskUseCase
from src.use_cases.tasks.get_task_by_id_use_case import GetTaskByIdUseCase
from src.use_cases.tasks.get_tasks_use_case import GetTasksUseCase
from src.use_cases.tasks.search_tasks_use_case import SearchTasksUseCase
from src.use_cases.tasks.update_task_use_case import UpdateTaskUseCase

task = Blueprint("task", __name__, url_prefix="/task")

repository = TaskRepository()


# This function is used to redirect the user to a specific route
def redirect_response(route: str):
    response = Response()
    response.headers["hx-redirect"] = url_for(route)
    return response


@task.route("/get", methods=["GET"])
@login_required
def get():

    use_case = GetTasksUseCase(current_user.id, repository)
    tasks = use_case.execute()

    return render_template(
        "partials/task-container.html", tasks=tasks, TaskStatus=TaskStatus
    )


@task.route("/get/<user_id>", methods=["GET"])
def get_by_id(user_id):
    use_case = GetTaskByIdUseCase(user_id, repository)
    task = use_case.execute()
    return {"task": "oi"}


@task.route("/search", methods=["GET"])
@login_required
def search():
    text = request.args.get("text-to-search")

    use_case = SearchTasksUseCase(current_user.id, repository)
    tasks = use_case.execute(text)

    return render_template(
        "partials/task-container.html", tasks=tasks, TaskStatus=TaskStatus
    )


@task.route("/add", methods=["POST"])
@login_required
def add():
    form = TaskForm()

    if form.validate_on_submit():
        use_case = AddTaskUseCase(current_user.id, form, repository)
        use_case.execute()

    return redirect(url_for("task.get"))


@task.route("/delete/<task_id>", methods=["DELETE"])
@login_required
def delete(task_id):
    print("id", task_id)
    use_case = DeleteTaskUseCase(task_id, repository)
    use_case.execute()

    return "", 200  # swap="delete" doesn't work with 204


@task.route("/get-update-form/<int:task_id>", methods=["GET", "PUT"])
@login_required
def get_update_form(task_id):
    form = TaskForm()

    use_case = GetTaskByIdUseCase(task_id, repository)
    task = use_case.execute()

    session["task_id"] = task_id

    task_data = {
        "title": task.title,
        "description": task.description,
        "due_date": task.due_date,
        "status": task.status,
    }

    form.process(data=task_data)

    return render_template("partials/update_form.html", form=form)


@task.route("/update", methods=["GET", "POST"])
@login_required
def update():
    form = TaskForm()

    task_id = session.get("task_id")

    new_task_data = {
        "title": form.data["title"],
        "description": form.data["description"],
        "due_date": form.data["due_date"],
        "status": form.data["status"],
    }

    use_case = UpdateTaskUseCase(task_id, new_task_data, repository)
    use_case.execute()

    session.pop("task_id")

    return redirect(url_for("task.get"))
