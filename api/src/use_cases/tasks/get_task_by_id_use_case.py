from src.repositories.task_repository import TaskRepository


class GetTaskByIdUseCase:
    def __init__(self, task_id: int, repository: TaskRepository):
        self.__repository = repository
        self.__task_id = task_id

    def execute(self):
        return self.__repository.get_task_by_id(self.__task_id)
