from flask import Blueprint, render_template, request, jsonify, flash, session, redirect, url_for
from models.usuario_model import usuarios
from controllers.usuario_reserva_controller import adicionar_total

servicos_controller = Blueprint('servicos', __name__)

@servicos_controller.route('/servicos')
def servicos():
    if session.get('nome') is None:
        flash("Você não está logado!")
        return redirect(url_for('cadastro.inicio')) 
    usuario = next((usuario for usuario in usuarios if usuario.nome == session.get('nome')), None)
    if usuario:
        flash(f'Total: {usuario.total}')
    return render_template('servicos.html')

@servicos_controller.route('/servicar', methods=['GET', 'POST'])
def servicar():
    if request.method == 'GET':
        return redirect(url_for('cadastro.inicio'))
    data = request.get_json()
    total = data['dados']['total']
    for usuario in usuarios:
        if usuario.nome == session.get('nome'):
            n = session.get('nome')
            adicionar_total(n, total)
    

    flash(f'Serviços selecionados! Custo total: R$ {total:.2f}')
    
    return jsonify({'redirect': '/servicos'}), 200