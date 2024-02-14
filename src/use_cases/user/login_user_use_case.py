

from src.repositories.user_repository import UserRepository
from src.server.server import engine

class LoginUserUseCase():
    
    def __init__(self, form):
        self.repository = UserRepository(engine)
        self.form = form
        
    def execute(self):
        database_pwd = self.repository.get_user_password_hash(self.form.email.data)
        
    def database_password_unhash(self):
        pass