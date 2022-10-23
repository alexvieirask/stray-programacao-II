''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Rota: [ auth_jwt_route ]
    descrição: 
    
    Testes:

'''
@app.route("/auth_jwt", methods=['POST'])
def auth_jwt_route():
    fields = request.get_json()
    username = fields["username"]
    password = fields["password"]

    if User.validate_login(username,password):
        user = db_query_by_username(username)
        access_token = create_access_token(identity = username)
        response =  jsonify({"result":"success", "detalhes": access_token}) 
    else: 
        response = jsonify({"result": "erro", "detalhes":"usuario ou senha incorreto(s)"})
    
    return response 