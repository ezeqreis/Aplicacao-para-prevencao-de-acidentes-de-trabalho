from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Acidente (db.Model):
    id= db.Column(db.Integer, primary_key=True)
    data = db.column(db.String(10), nullable=False)
    horario = db.column(db.string(5), nullable=False)
    local = db.Column(db.string(100), nullable=False)
    sexo = db.Column(db.string(1), nullable=False)
    nome = db.column(db.String(100), nullable=False)
    matricula = db.column(db.String(20), nullable=False)
    idade = db.column(db.Integer, nullable=False)
    parte_corpo = db.Column(db.string(50), nullable=False)
    afastamento = db.Column(db.Boolean, nullable=False)