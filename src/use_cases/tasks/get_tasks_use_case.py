from src.repositories.task_repository import TaskRepository


class GetTasksUseCase():
    def __init__(self, user_id, repository: TaskRepository):
        self.__user_id = user_id
        self.__repository = repository

    def get_active_tasks(self):
        return self.__repository.get_active_tasks(self.__user_id)

    def get_deleted_tasks(self):
        return self.__repository.get_deleted_tasks(self.__user_id)