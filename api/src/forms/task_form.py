from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class TaskForm(FlaskForm):
    """
    Form for the Task model.

    Class that herits from FlaskForm and has the some fields of the Task model as inputs. This class will be used to create the form for the user to create a new task. It won't need to write the form in HTML, because Flask will do it for us.

    It contains the csrf_token, which is a security token that Flask uses to protect the form from CSRF attacks, as a hidden field.

    Attributes:
        title: A StringField with the label "Titulo: ".
        description: A StringField with the label "Descrição: ".
        due_date: A DateField with the label "Para: ".
        status: A SelectField with the label "Status: ".
        submit: A SubmitField with the label "Enviar".
    """

    title = StringField("Titulo: ", validators=[DataRequired(), Length(max=50)])

    description = TextAreaField("Descrição: ", validators=[DataRequired()])

    due_date = DateField("Para (opcional): ", validators=[Optional()])

    status = SelectField(
        "Status: ",
        choices=[(0, "Não comecei"), (1, "Fazendo"), (2, "Terminado")],
        validators=[DataRequired()],
    )

    submit = SubmitField("Enviar")
