from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.usuario_model import usuarios
from datetime import timedelta
from dotenv import load_dotenv
from werkzeug.security import check_password_hash
import os
import base64, hashlib


login_controller = Blueprint('login', __name__)

@login_controller.route('/login', methods=['GET', 'POST'])
def login():
    # Limpar as variáveis de ambiente existentes
    for key in list(os.environ.keys()):
        if key.startswith('SENHA') or key.startswith('USUARIO'):
            del os.environ[key]

    # Caminho para o arquivo .env
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    print(f"Carregando o .env de: {dotenv_path}")  # Verifique o caminho do arquivo

    # Carregar o arquivo .env
    load_dotenv(dotenv_path=dotenv_path, override=True)

    # Verificar se as variáveis de ambiente foram carregadas corretamente
    senhas = {}
    nomes = {}

    for key, value in os.environ.items():
        if key.startswith('SENHA'):
            senhas[key] = value
        elif key.startswith('USUARIO'):
            nomes[key] = value

    # A lógica do login
    if session.get('nome') is None:
        if request.method == 'POST':
            nome = request.form['nome']
            senha = request.form['senha']
            senhaCriptografada = base64.b64encode(hashlib.sha256(senha.encode()).digest()).decode()

            # Verifique se o nome e senha são válidos
            for key, value in nomes.items():
                if value == nome:
                    senha_key = f'SENHA{key[-1]}'
                    if value == 'admin':
                        senha_key = f'SENHA'
                    if senha_key in senhas:
                        if check_password_hash(senhas[senha_key], senhaCriptografada):
                            session['nome'] = nome
                            session.permanent = True
                            return redirect(url_for('cadastro.inicio'))
            flash('Nome ou senha incorretos!')
        return render_template('login.html')
    else:
        flash('Você já está logado!')
        return redirect(url_for('cadastro.inicio'))

@login_controller.route('/logout')
def logout():
    session.pop('nome', None)
    return redirect(url_for('login.login'))

