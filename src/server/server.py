from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente no .eInv

app = Flask(__name__,
            template_folder="../templates",
            static_folder="../static")

csrf = CSRFProtect(app)


# Capturando as variáveis de ambiente configuradas
USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

# Configurando a URI do banco de dados com as credenciais fornecidas
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USER}:{PASSWORD}@localhost/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345'
app.config['WTF_CSRF_SECRET_KEY'] = '12345'

# Se conectando ao banco de dados
db = SQLAlchemy()
db.init_app(app)
engine = create_engine(
    f'mysql+pymysql://{USER}:{PASSWORD}@localhost/{DATABASE}')

with app.app_context():
    from src.models.task import Task
    from src.models.user import User

    # Cria as tabelas
    db.create_all()
    print("As tabelas 'user' e 'task' foram criadas com sucesso.")


def register_blueprints(app):
    from src.routes import routes
    app.register_blueprint(routes.bp)


register_blueprints(app)
