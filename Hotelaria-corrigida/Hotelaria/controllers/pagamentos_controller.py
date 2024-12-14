from flask import Blueprint, render_template, request, jsonify, flash, session, redirect, url_for
from models.usuario_model import usuarios

pagamentos_controller = Blueprint('pagamentos', __name__)

@pagamentos_controller.route('/pagamentos')
def pagamentos():
    if session.get('nome') != 'admin':
        flash("Você não é um funcionário!")
        return redirect(url_for('cadastro.inicio'))
    return render_template('pagamentos.html', usuarios = usuarios)

@pagamentos_controller.route('/pagar', methods=['GET','POST'])
def pagar():
    if request.method == 'GET':
        return redirect(url_for('cadastro.inicio'))
    print('PAGANDO')
    data = request.get_json()
    nome = data.get('nomeUsuario')
    for usuario in usuarios:
        if usuario.nome == nome:
            usuario.total = 0
            return jsonify({'redirect': '/'}), 200