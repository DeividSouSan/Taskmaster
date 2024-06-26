from src.repositories.task_repository import TaskRepository


class DeleteTaskUseCase:
    def __init__(self, task_id: int, repository: TaskRepository):
        self.__task_id = task_id
        self.__repository = repository

    def execute(self):
        return self.__repository.delete_task(self.__task_id)
