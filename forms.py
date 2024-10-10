from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class AcidenteForm(FlaskForm):
    data=StringField('Data (AAAA-MM-DD)', validators=[DataRequired(), Length(max=10)])
    horario=StringField('Horário (HH:MM )', validators=[DataRequired(), Length(max)])
    local=StringField('Local', validators=[DataRequired(), Length (max-100)])
    sexo=SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), Validators]),
    nome=StringField('Nome', validators=[DataRequired(), Length(max=100)]),
    matricula=StringField('Matricula', validators-[DataRequired(), Length(max=20)]),
    idade=IntegerField('Idade', validators=[DataRequired()]),
    parte_corpo = StringField('Parte do Corpo Atingida', validators=[DataRequired(),Length]),
    afastamento = BooleanField('Afastamento do Trabalho'),
    submit = SubmitField('Enviar'),