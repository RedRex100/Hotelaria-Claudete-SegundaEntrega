from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify
from models.usuario_model import usuarios


checkout_controller = Blueprint('checkout', __name__)

@checkout_controller.route('/registros')
def registros():
    if session.get('nome') is None:
        flash("Você não está logado!")
        return redirect(url_for('cadastro.inicio'))
    usuario = next((usuario for usuario in usuarios if usuario.nome == session.get('nome')), None)
    if usuario:
        return render_template('registro.html', reservas=usuario.reservas)
    
    flash("Usuário não encontrado.")
    return redirect(url_for('cadastro.inicio'))

@checkout_controller.route('/checkout')
def checkout():
    if session.get('nome') is None:
        flash("Você não está logado!")
        return redirect(url_for('cadastro.inicio'))
    for usuario in usuarios:
        if usuario.nome == session.get('nome'): 
            if usuario.total == 0:
                return render_template('checkout.html', reservas=usuario.reservas, usuario=usuario)
            else:
                flash("Você não quitou suas dívidas!")
                return redirect(url_for('cadastro.inicio'))

@checkout_controller.route('/checkoutar', methods=['GET', 'POST'])
def checkoutar():
    if request.method == 'GET':
        return redirect(url_for('cadastro.inicio'))
    for usuario in usuarios:
        if usuario.nome == session.get('nome'):
            usuario.reservas = []
            return jsonify({'redirect': '/registros'}), 200