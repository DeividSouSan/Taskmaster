from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    """
    Form for the login of the User.
    
    Class that herits from FlaskForm and has the fields of the User model as inputs. This class will be used to create the form for the user to login. It won't need to write the form in HTML, because Flask will do it for us.
    
    It contains the csrf_token, which is a security token that Flask uses to protect the form from CSRF attacks, as a hidden field.
    
    Attributes:
        username: A StringField with the label "Nome de Usuário: ".
        password: A PasswordField with the label "Senha: ".
        submit: A SubmitField with the label "Entrar".
    
    """

    username = StringField("Nome de Usuário", validators=[DataRequired()])

    password = PasswordField(
        "Senha", validators=[DataRequired(), Length(min=8, max=20)]
    )

    submit = SubmitField("Entrar", render_kw={"disabled": "true"})
