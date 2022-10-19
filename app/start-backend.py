''' Importações das configurações e serviços  '''
from services.config import *
from services.database__init__ import *

''' Importação das rotas '''
from routes import *

''' Rota: [ home_route ]
    descrição: 
'''
@app.route("/")
def home_route():    
    return render_template('pages/home.html')

if __name__ == "__main__":
    app.run(debug=True)