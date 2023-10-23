from flask import render_template, request, redirect, session, flash, url_for
from main import app, db
from models.pessoa import Pessoa
from models.usuario import Usuarios
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash



@app.route('/')
def inicio():
    lista = Pessoa.query.order_by(Pessoa.id)
    return render_template('lista.html', titulo='Lista de Alunos', pessoas = lista)

@app.route('/novo')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proximo = url_for('inicio')))
    return render_template('novo.html', titulo='criar pessoa')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome'].capitalize()
    idade = request.form['idade']
    altura = request.form['altura']

    pessoa = Pessoa.query.filter_by(nome=nome).first()
    if pessoa:
        flash("Este usuário já existe")
        return redirect(url_for('lista'))
    nova_pessoa = Pessoa(nome=nome, idade=idade, altura=altura)
    db.session.add(nova_pessoa)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    #fazer uma query do banco
    pessoa = Pessoa.query.filter_by(id=id).first()
    return render_template('editar.html', titulo= 'Editar Pessoa', pessoa = pessoa)

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))

    Pessoa.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Pessoa deletada com sucesso')
    return redirect(url_for('inicio'))


@app.route('/atualizar', methods=['POST'])
def atualizar():
    # Obter os dados enviados pelo formulário
    nome = request.form['nome']
    idade = request.form['idade']
    altura = request.form['altura']
    
    # Encontrar a pessoa pelo nome
    pessoa = Pessoa.query.filter_by(nome=nome).first()
    if pessoa:
        # Atualizar os dados da pessoa
        pessoa.idade = idade
        pessoa.altura = altura
        # Commit para salvar as alterações no banco de dados
        db.session.commit()
        flash('Dados atualizados com sucesso!')
    else:
        flash('Pessoa não encontrada.')
    
    # Redirecionar de volta para a página principal
    return redirect(url_for('inicio'))


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome_usuario = request.form.get('username').lower()
        senha_usuario = request.form.get('password')
        # verificar se o usuário já existe no banco de dados
        existe_usuario = Usuarios.query.filter_by(nome=nome_usuario).count()
        if existe_usuario > 0:
            flash("NOME DE USUARIO JA CADASTRADO")
            return render_template('registrar.html')
        # criar novo usuário
        else:
            try:
                senha_criptografada = generate_password_hash(senha_usuario)
                novo_usuario = Usuarios(nome=nome_usuario, senha=senha_criptografada)
                db.session.add(novo_usuario)
                db.session.commit()
                flash("Registro de novo usuário realizado com sucesso")
                return redirect(url_for('inicio'))
            except:
                flash("Erro ao cadastrar novo usuário")
    else:
        return render_template('registrar.html')
        
@app.route('/login')
def login():
    proximo = request.args.get('proximo')
    return render_template('login.html', proximo=proximo)

    
@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nome=request.form['usuario']).first()
    if usuario:
        if check_password_hash(usuario.senha, request.form['senha']):
            session['usuario_logado'] = usuario.nome
            flash(usuario.nome + ' Logado com sucesso')
            proxima_pagina = request.form['proximo']
            return redirect(proxima_pagina)
    flash("Usuário ou senha inválidos!!")
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('voce foi Desconectado')

    return redirect(url_for('login'))
