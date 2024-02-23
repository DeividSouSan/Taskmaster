from typing import Protocol
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class ILoginForm(Protocol):
    username: StringField
    password: PasswordField
    submit: SubmitField

class LoginForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired()])

    password = PasswordField(
        "Senha",
        validators=[DataRequired(), Length(min=8, max=20)])

    submit = SubmitField("Entrar")
