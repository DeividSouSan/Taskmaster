from src.forms.task_form import TaskForm
from src.models.task import Task
from src.repositories.task_repository import TaskRepository


class AddTaskUseCase:
    def __init__(self, user_id: int, form: TaskForm, repository: TaskRepository):
        self._user_id = user_id
        self._form = form
        self._repository = repository

    def execute(self):
        task = self._create_object(self._form)
        self._repository.add_task(task)

    def _create_object(self, form):
        return Task(
            user_id=self._user_id,
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            status=int(form.status.data),
        )
