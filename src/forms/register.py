from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username: str = StringField(
        "Nome de Usuário: ",
        validators=[DataRequired(),  Length(max=20)])

    password: str = PasswordField(
        "Senha: ",
        validators=[DataRequired(), Length(min=8, max=20)])

    fullname: str = StringField(
        "Nome Completo: ",
        validators=[DataRequired(), Length(max=50)])

    email: str = EmailField(
        "E-mail: ",
        validators=[DataRequired(), Length(max=50)])
