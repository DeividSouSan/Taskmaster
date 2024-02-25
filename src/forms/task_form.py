from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    task_title = StringField(
        "Titulo: ",
        validators=[DataRequired(), Length(50)])

    task_description = TextAreaField(
        "Descrição: ",
        validators=[DataRequired()])

    due_date = DateField("Para: ")

    status = SelectField("Status: ",
                         choices=["Não comecei", "Fazendo", "Terminado"],
                         validators=[DataRequired()])

    submit = SubmitField("Enviar")
