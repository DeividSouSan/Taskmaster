from typing import Protocol

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    """
    Form for the registering the User.
    
    Class that herits from FlaskForm and has the fields of the User model as inputs. This class will be used to create the form for the user to register a new user. It won't need to write the form in HTML, because Flask will do it for us.
    
    It contains the csrf_token, which is a security token that Flask uses to protect the form from CSRF attacks, as a hidden field.
    
    Attributes:
        username: A StringField with the label "Nome de Usuário: ".
        password: A PasswordField with the label "Senha: ".
        fullname: A StringField with the label "Nome Completo: ".
        email: A EmailField with the label "E-mail: ".
        submit: A SubmitField with the label "Enviar".
    
    """
    
    username = StringField(
        "Nome de Usuário: ", validators=[DataRequired(), Length(max=20)]
    )

    password = PasswordField(
        "Senha: ", validators=[DataRequired(), Length(min=8, max=20)]
    )

    fullname = StringField(
        "Nome Completo: ", validators=[DataRequired(), Length(max=50)]
    )

    email = EmailField("E-mail: ", validators=[DataRequired(), Length(max=50)])

    submit = SubmitField("Enviar", render_kw={"disabled": "true"})
