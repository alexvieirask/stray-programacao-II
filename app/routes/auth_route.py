''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Rota: [ auth_jwt_route ]
    descrição: Esta rota realiza a criação do TOKEN JWT.
    
    Testes:        
        1. curl -H \Content-Type:application/json\ -X POST --data "{\"username\":\"emanoela.erthal\",\"password\":\"my-password2\"}" http://localhost:5000/auth_jwt

        2. curl localhost:5000/[Rota Protegida] -H 'Authorization: Bearer [ TOKEN GERADO ]'

'''
@app.route("/auth_jwt", methods=['POST'])
def auth_jwt_route():
    fields = request.get_json()

    if User.validate_login(fields["username"],fields["password"]):
        
        access_token = create_access_token(identity = fields["username"])
        
        response =  jsonify({"result":"success", "detalhes": access_token}) 
    else: 
        response = jsonify({"result": "erro", "detalhes":"usuario ou senha incorreto(s)"})
    
    return response 