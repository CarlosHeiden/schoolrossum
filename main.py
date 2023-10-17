import socket
from flask import Flask, render_template, request, redirect, session, flash, url_for
from models.pessoa import Pessoa
from models.usuario import Usuarios
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "123456"

SQLAlchemy_DATABASE_URL = "sqlite:///C:home/carlos/Documentos/APEX/PYTHON/flask/schoolrossum/banco/aplication.sqlite3"
db = SQLAlchemy(app)

lista = Pessoa.query.order_by(Pessoa.id)

@app.route('/')
def inicio():
    lista = Pessoa.query.order_by(Pessoa.id)
    return render_template('lista.html', titulo='Lista de Alunos', pessoas = lista)

@app.route('/novo')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('novo')))
    return render_template('novo.html', titulo='Cadastro de alunos')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    if pessoa:
        flash("Este usuário já existe")
        return redirect(url_for('lista'))
    nova_pessoa = Pessoa(nome=nome, idade=idade, altura=altura)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('lista'))

@app.route('/login')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', titulo = "Software Tech", proximo=proximo)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.qyery.filter_by(nickname=request.form['usuario'])
    if usuario:
        if request.form['senha']==usuario.senha:
            session['usuario_logado'] ==usuario.nickname
            flash(usuario.nickname + 'Logado com sucesso')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
    flash("Ususrio ou senha invalidos!!")
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session["usuario_logado"]== None
    flash("Voce foi deslogado")
    return redirect(url_for('login'))

def get_server_ip():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    return server_ip


server_ip = get_server_ip()
print(server_ip)
app.run(host=f"{server_ip}", port=80, debug=True)