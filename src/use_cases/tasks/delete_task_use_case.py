from src.repositories.task_repository import TaskRepository


class MoveTaskToTrashUseCase:
    def __init__(self, task_id, repository: TaskRepository):
        self.__task_id = task_id
        self.__repository = repository

    def move_task_to_trash(self):
        return self.__repository.move_to_trash(self.__task_id)
