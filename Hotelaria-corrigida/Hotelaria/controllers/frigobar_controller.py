from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models.usuario_model import usuarios
from controllers.usuario_reserva_controller import adicionar_total

frigobar_controller = Blueprint('frigobar', __name__)

@frigobar_controller.route('/frigobar')
def frigobar():
    if session.get('nome') is None:
        flash("Você não está logado!")
        return redirect(url_for('cadastro.inicio'))
    usuario = next((usuario for usuario in usuarios if usuario.nome == session.get('nome')), None)
    if usuario:
        flash(f'Total: R${usuario.total}')
    return render_template('frigobar.html')

@frigobar_controller.route('/frigobarar', methods=['GET', 'POST'])
def frigobarar():
    if request.method == 'GET':
        return redirect(url_for('cadastro.inicio'))
    data = request.get_json()
    total = data['dados']['total']
    for usuario in usuarios:
        if usuario.nome == session.get('nome'):
            n = session.get('nome')
            adicionar_total(n, total)
    

    flash(f'Serviços selecionados! Custo total: R$ {total:.2f}')
    
    return jsonify({'redirect': '/frigobar'}), 200