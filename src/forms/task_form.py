from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class TaskForm(FlaskForm):
    title = StringField("Titulo: ", validators=[
                        DataRequired(), Length(max=50)])

    description = TextAreaField("Descrição: ", validators=[DataRequired()])

    due_date = DateField("Para: ", validators=[Optional()])

    status = SelectField("Status: ",
                         choices=[(0, "Não comecei"),
                                  (1, "Fazendo"),
                                  (2, "Terminado")],
                         validators=[DataRequired()])

    submit = SubmitField("Enviar")
