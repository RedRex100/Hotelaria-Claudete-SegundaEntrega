from flask import Flask
from datetime import timedelta


app = Flask(__name__, template_folder= 'Arquivos')
app.secret_key = '67bvchgjydDfsfk??;'

from controllers import *

app.register_blueprint(cadastro_controller)
app.register_blueprint(checkout_controller)
app.register_blueprint(frigobar_controller)
app.register_blueprint(login_controller)
app.register_blueprint(pagamentos_controller)
app.register_blueprint(reservas_controller)
app.register_blueprint(servicos_controller)


app.permanent_session_lifetime = timedelta(minutes=5)

if __name__ == '__main__':
    app.run(debug=False)