from src.models.task import Task
from src.forms.task_form import TaskForm
from src.repositories.task_repository import TaskRepository


class AddTaskUseCase:
    def __init__(self, user_id: int, form: TaskForm, repository: TaskRepository):
        self.__user_id = user_id
        self.__form = form
        self.__repository = repository

    def add_task(self):
        task = self._set_task()
        self.__repository.add_task(task)

    def _set_task(self):
        return Task(
            user_id=self.__user_id,
            title=self.__form.title.data,
            description=self.__form.description.data,
            due_date=self.__form.due_date.data,
            status=int(self.__form.status.data),
            deleted=False
            )
        
