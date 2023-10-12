from flask import Flask, render_template, request, redirect, session, flash
from pessoa import Pessoa

pessoa1 = Pessoa("Rodrigo", 32, 1.87)
pessoa2 = Pessoa("Maria", 45, 1.69)
pessoa3 = Pessoa("Anna", 44, 1.78)
pessoa4 = Pessoa("Joao", 35, 1.87)
pessoa5 = Pessoa("Orlando", 88, 1.79)

lista = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5]

app = Flask(__name__)

app.secret_key = "123456"

@app.route('/')
def inicio():
    return render_template('lista.html', titulo='Lista de Alunos', pessoas = lista)

@app.route('/novo')
def cadastro():
    return render_template('novo.html', titulo='Cadastro de alunos')

@app.route('/editar')
def editar():
    return render_template('editar.html', titulo='Editar aluno')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas = Pessoa(nome, idade, altura)
    lista.append(pessoas)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo = "Software Tech")

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123456' == request.form['senha']:
        session["usuario_logado"] = request.form['usuario']
        flash(session['usuario_logado'] + "voce esta logado")
        return redirect('/')
    else:
        flash("Usuario ou senha invalidos, tente novamente")
        return redirect('/login')

@app.route('/logout')
def logout():
    session["usuario_logado"]== None
    flash("Voce foi deslogado")
    return redirect('/')


app.run(debug=True)