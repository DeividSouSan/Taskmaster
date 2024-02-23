from ...utils.password_hasher import PassowordHash
from ...forms.login_form import ILoginForm
from ...repositories.user_repository import IUserRepository
from flask_login import login_user

# Vou ter que verificar as credenciais que foram enviadas
# Se estiverem corretas eu utilizo elas para acessar o repositório
# Do repositório eu pegos os dados do usuário e instâncio User com esses dados
# Depois eu utilizo a função login_user do flask_login para logar o usuário


class LoginUserUseCase():

    def __init__(self, form: ILoginForm, repository: IUserRepository):
        self.__repository = repository
        self.__form = form

    def attempt_login_user(self):
        username = self.__form.username.data
        password = self.__form.password.data


        valid_credentials = self.verify_credentials(username, password)

        if valid_credentials:
            user = self.__repository.get_user_by_username(username)

            login_user(user)
            return True
        
        return False

    def get_user(self):
        pass

    def verify_credentials(self, username, password):

        if self.__repository.exists_user_with_field("username", username):
            hashed_password = self.__repository.get_user_password_by_username(username)
            correct_password = PassowordHash().check_password(password, hashed_password)

            if correct_password:
                return True

        return False
