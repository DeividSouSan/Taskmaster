from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
import os

load_dotenv() # Carrega as variáveis de ambiente no .env

app = Flask("__name__")

# Capturando as variáveis de ambiente configuradas
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

# Acessando o banco de dados com as credenciais fornecidas
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER}:{PASSWORD}@localhost/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    from src.models.task import Task
    from src.models.user import User
    db.create_all()
    print("As tabelas 'user' e 'task' foram criadas com sucesso.")


from src.routes import routes
app.register_blueprint(routes.bp)
