from src.repositories.user_repository import UserRepository
from src.models.user import User
from src.server.server import engine
from datetime import datetime
import bcrypt


class RegisterUserUseCase():

    def __init__(self, form):
        self.repository = UserRepository(engine)
        self.form = form
        self.error = None

    def execute(self):
        username = self.form.username.data
        email = self.form.email.data

        invalid_user = self.repository.exists_user_with_username(username)
        invalid_email = self.repository.exists_user_with_email(email)

        if invalid_user:
            self.error = {
                "type": "username",
                "text": "Já existe um usuário com esse nome."
            }

            return False

        if invalid_email:
            self.error = {
                "type": "email",
                "text": "Já existe um usuário com esse email."
            }

            return False

        bytes_pw = bytes(self.form.password.data, "utf-8")
        password_hash = bcrypt.hashpw(bytes_pw, bcrypt.gensalt())

        user = User(
            username=self.form.username.data,
            password_hash=password_hash,
            fullname=self.form.fullname.data,
            email=self.form.email.data,
            registration=datetime.now(),
            tasks=[]
        )

        self.repository.add_user(user)
        return True
