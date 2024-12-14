from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from controllers.usuario_reserva_controller import adicionar_usuario
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from models.usuario_model import usuarios
import os

load_dotenv()

cadastro_controller = Blueprint('cadastro', __name__)

@cadastro_controller.route('/')
def inicio():
    usuario1 = os.getenv('USUARIO1')
    senha1 = os.getenv('SENHA')
    adicionar_usuario(usuario1, '', '', '', '', senha1)
    return render_template('inicio.html')

@cadastro_controller.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@cadastro_controller.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return redirect(url_for('cadastro.inicio'))
    
    # Obter os dados do formulário
    data = request.get_json()
    nome = data.get('nome')
    endereco = data.get('endereco')
    cpf = data.get('cpf')
    telefone = data.get('telefone')
    email = data.get('email')
    senha = data.get('senha')
    hashed_senha = generate_password_hash(senha)

    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')

    load_dotenv(dotenv_path=dotenv_path, override=True)

    with open(dotenv_path, 'r') as f:
        linhas = f.readlines()
        contador = sum(1 for linha in linhas if linha.startswith('SENHA'))

    # Adicionar a nova SENHA no arquivo .env
    with open(dotenv_path, 'a') as f:
        f.write(f'\nSENHA{contador+1}={hashed_senha}\n')

    # Adicionar o USUARIO no arquivo .env
    with open(dotenv_path, 'a') as f:
        f.write(f'USUARIO{contador+1}={nome}\n')

    adicionar_usuario(nome, endereco, cpf, telefone, email, hashed_senha)
    return jsonify({"redirect": "/login"}), 200
