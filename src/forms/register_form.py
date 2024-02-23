from typing import Protocol
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length


class IRegisterForm(Protocol):
    email: EmailField
    password: PasswordField
    full_name: StringField
    email: EmailField
    submit: SubmitField

class RegisterForm(FlaskForm):
    username = StringField(
        "Nome de Usuário: ",
        validators=[DataRequired(),  Length(max=20)])

    password = PasswordField(
        "Senha: ",
        validators=[DataRequired(), Length(min=8, max=20)])

    fullname = StringField(
        "Nome Completo: ",
        validators=[DataRequired(), Length(max=50)])

    email = EmailField(
        "E-mail: ",
        validators=[DataRequired(), Length(max=50)])

    submit = SubmitField("Enviar")
