from src.repositories.task_repository import TaskRepository


class UpdateTaskUseCase:
    def __init__(self, task_id: int, new_values: dict[str, any], repository: TaskRepository):
        self._task_id = task_id
        self._new_values = new_values
        self._repository = repository

    def execute(self):
        return self._repository.update_task(self._task_id, self._new_values)
