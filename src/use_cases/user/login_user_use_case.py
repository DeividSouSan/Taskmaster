from ...forms.login_form import ILoginForm
from ...repositories.user_repository import IUserRepository


class LoginUserUseCase():

    def __init__(self, form: ILoginForm, repository: IUserRepository):
        self.__repository = repository
        self.__form = form

    def execute(self):
        pass

    def database_password_unhash(self):
        pass
