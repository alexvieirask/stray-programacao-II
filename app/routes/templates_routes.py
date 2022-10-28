from services.config import *
from services.utils import *

''' Rota: [ home_route ]
    descrição: Retorna o template da tela inicial da aplicação.
'''
@app.route("/")
def home_route():
    return render_template("pages/home.html")

''' Rota: [ join_route ]
    descrição: Retorna o template da tela de registro.
'''
@app.route("/join")
def join_route():
    return render_template("pages/register.html")

''' Rota: [ login_route ]
    descrição: Retorna o template da tela de login.
'''
@app.route("/login")
def login_route():
    return render_template("pages/login.html")