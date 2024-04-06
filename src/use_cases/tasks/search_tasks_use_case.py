
from src.repositories.task_repository import TaskRepository


class SearchTasksUseCase:
    def __init__(self, user_id: int, repository: TaskRepository):
        self.__user_id = user_id
        self.__repository = repository

    def execute(self, text):
        return self.__repository.get_tasks_like(self.__user_id, text)
