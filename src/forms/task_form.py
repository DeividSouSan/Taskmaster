from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):
    task_title = StringField(
        "Titulo: ",
        validators=[DataRequired(), Length(max=50)])

    task_description = TextAreaField(
        "Descrição: ",
        validators=[DataRequired()])

    due_date = DateField("Para: ")

    status = SelectField("Status: ",
                         choices=[(0, "Não comecei"),
                                  (1, "Fazendo"),
                                  (2, "Terminado")],
                         validators=[DataRequired()])

    submit = SubmitField("Enviar")
