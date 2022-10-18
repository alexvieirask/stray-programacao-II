''' Importações das configurações e serviços  '''
from services.config import *
from services.database__init__ import *
from services.utils import db_query_all

''' Importação das rotas '''
from routes import *

''' Rota: [ home_route ]
    descrição: 
'''
@app.route("/")
def home_route():    
    games = db_query_all(Game)
    return render_template('pages/home.html',games = games)

if __name__ == "__main__":
    app.run(debug=True)