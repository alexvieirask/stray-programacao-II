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
        purchases_in_order_asc = sorted(user.purchases)

        games_buyed = [ index.game.json() for index in purchases_in_order_asc ]
        purchases_json  = [ purchase.json() for purchase in purchases_in_order_asc ]
        
        
        response = jsonify({"result":"ok", "details": {"games":games_buyed, "purchases" : purchases_json}})

    
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response

@app.route("/user/giftcards")
@jwt_required()
def user_available_giftcards_route():
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username)  
        
        all_giftcards = [ giftcard.json() for giftcard in user.giftcards]
    
        response = jsonify({"result":"ok", "details": all_giftcards})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response