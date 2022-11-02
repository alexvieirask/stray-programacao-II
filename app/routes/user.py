from services.config import *
from services.utils import *

''' Rota: [ user_info_route ]
    descrição: Retorna todos os dados do usuário logado.

    Testes:
        1. curl localhost:5000/user/info -H "Authorization:Bearer "TOKEN_JWT"
    
    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/user/info")
@jwt_required()
def user_info_route(): 
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username) 
        
        response = jsonify({"result":"ok", "details": user.json()})

    
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response



''' Rota: [ user_library_route ]
    descrição: Retorna todos os jogos comprados do usuário logado.

    Testes: 
        1. curl localhost:5000/user/library -H "Authorization:Bearer "TOKEN_JWT"

'''
@app.route("/user/library")
@jwt_required()
def user_library_route(): 
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username) 

        games_buyed = [ index.game.json() for index in user.purchases ]
        
        response = jsonify({"result":"ok", "details": games_buyed})

    
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response