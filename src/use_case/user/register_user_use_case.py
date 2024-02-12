from src.repositories.user_repository import UserRepository
from src.models.user import User
from src.server.server import engine
from datetime import datetime
import bcrypt


class RegisterUserUseCase():

    def __init__(self, form):
        self.form = form

    def execute(self):
        repository = UserRepository(engine)

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

        repository.add_user(user)
