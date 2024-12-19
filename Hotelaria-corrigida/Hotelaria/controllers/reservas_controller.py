from flask import Blueprint, render_template, request, jsonify, flash, session, redirect, url_for
from models.reserva_model import Reserva
from controllers.usuario_reserva_controller import adicionar_reserva_usuario, adicionar_total

reservas_controller = Blueprint('reservas', __name__)

def obter_total_reservas():
    return 100

@reservas_controller.route('/reservar', methods=['GET', 'POST'])
def reservar():
    if request.method == 'GET':
        return redirect(url_for('cadastro.inicio'))
    data = request.get_json()
    nome = data.get('nome')
    quarto = int(data.get('quarto'))
    pagamento = data.get('formapagamento')
    diferenca = data.get('diferenca')
    data1 = data.get('data1')
    data2 = data.get('data2')

    if quarto <= 0 or quarto > 120:
        return jsonify({"message": "Número do quarto inválido! O número do quarto deve ser maior que 0 e no máximo 120."}), 400

    total_reservas = obter_total_reservas()
    if total_reservas >= 120:
        return jsonify({"message": "Número máximo de reservas alcançado"}), 400

    nova_reserva = Reserva(nome, quarto, pagamento, diferenca, data1, data2)
    adicionar_reserva_usuario(nome, nova_reserva)
    adicionar_total(nome, diferenca*300)

    return jsonify({"redirect": "/registros"}), 200

@reservas_controller.route('/reservas')
def reservas():
    if session.get('nome') is None:
        flash("Você não está logado!")
        return redirect(url_for('cadastro.inicio'))
    return render_template('reservas.html')
