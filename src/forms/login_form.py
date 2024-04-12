from typing import Protocol

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):

    username = StringField("Nome de Usuário", validators=[DataRequired()])

    password = PasswordField(
        "Senha", validators=[DataRequired(), Length(min=8, max=20)]
    )

    submit = SubmitField("Entrar", render_kw={"disabled": "true"})
