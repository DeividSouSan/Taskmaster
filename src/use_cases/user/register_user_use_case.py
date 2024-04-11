from datetime import datetime

from flask import flash

from ...models.user import User
from ...repositories.user_repository import UserRepository
from ...utils.user_registration_notifier import UserRegistrationNotifier


class RegisterUserUseCase:
    repository: UserRepository
    notifier: UserRegistrationNotifier

    def __init__(self, repository: UserRepository, notifier: UserRegistrationNotifier):
        self.__repository = repository
        self.__notifier = notifier

    def attempt_registration(self, user: User) -> bool:
        if field_name := self.__check_unique_fields(user):
            notify = {
                "username": self.__notifier.notify_username_alredy_used,
                "email": self.__notifier.notify_email_already_used,
            }

            notify[field_name]()
            return False
        
        self.__repository.add_user(user)
        self.__notifier.notify_successful_register()
        return True
    
    def __check_unique_fields(self, user: User) -> str | None:
        
        unique_fields = [
            {"field_name": "username", "value": user.username},
            {"field_name": "email", "value": user.email},
        ]
        
        for field in unique_fields:
            if self.__repository.exists_user_with_field(field["field_name"], field["value"]):
                return field["field_name"]
                