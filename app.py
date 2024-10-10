from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import AcidenteForm
from models import db, Acidente
from config import Config

app=Flask(name)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    acidentes= Acidente.query.all()
    return render_template('index.html', acidentes-acidentes)

@app.route('/novo_acidente', methods=['GET', 'POST'])
def novo_acidente():
    form=AcidenteForm()
    if form.validate_on_submit():
        novo_acidente = Acidente(
            data=form.data.data,
            horario=form.horario.data,
            local=form.local.data,
            sexo=form.sexo.data,
            nome=form.nome.data,
            matricula=form.matricula.data,
            idade=form.idade.data,
            parte_corpo=form.parte_corpo.data,
            afastamento=form.afastamento.data
        )
        db.session.add(novo_Acidente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('novo_acidente.html', form=form)

if _name_=='_main_':
    app.run(debug=True)