from typing import Protocol
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class ILoginForm(Protocol):
    email: EmailField
    password: PasswordField
    submit: SubmitField

class LoginForm(FlaskForm):

    email = EmailField(
        "E-mail",
        validators=[DataRequired()])

    password = PasswordField(
        "Senha",
        validators=[DataRequired(), Length(min=8, max=20)])

    submit = SubmitField("Entrar")
