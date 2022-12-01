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

''' Rota: [ user_library_route ]
    descrição: Retorna todos os giftcards comprados do usuário logado.
'''
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

''' Rota: [ user_library_route ]
    descrição: Realiza a alteração das informações do usuário logado.
'''
@app.route("/user/update", methods = ["POST"])
@jwt_required()
def user_update_route():
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username)
        fields = request.get_json()
        exceptions = []
        
        MIN_CHARACTERS_FIELDS = 5
        MAX_CHARACTERS_NAME_OR_USERNAME_INPUT = 50
        MAX_CHARACTERS_DESCRIPTION_INPUT = 100

        ''' Validação dos Campos '''
        for field in fields:
            if len(fields[field]) < MIN_CHARACTERS_FIELDS:
                exception = { "type":"input_field", "details":"The #input_{} don't have minimal length. Minimal is {} Characters.".format(field,MIN_CHARACTERS_FIELDS)}
                exceptions.append(exception)
            
            if (field == "name" or field == "username") and len(fields[field]) > MAX_CHARACTERS_NAME_OR_USERNAME_INPUT:
                print(len(fields[field]))
                exception = { "type":"input_field", "details":"The #input_{} exceeded the maximum number of characters allowed. Max is {} Characters.".format(field, MAX_CHARACTERS_NAME_OR_USERNAME_INPUT)}
                exceptions.append(exception)

            if field == "description" and len(fields[field]) > MAX_CHARACTERS_DESCRIPTION_INPUT:
                exception = { "type":"input_field", "details":"The #input_{} exceeded the maximum number of characters allowed. Max is {} Characters.".format(field, MAX_CHARACTERS_DESCRIPTION_INPUT)}
                exceptions.append(exception)
            

        ''' Validação de disponibilidade de username '''
        if fields["username"] != user.username:
            user_exists = db_check_if_username_exists(User,fields["username"])
        
            if user_exists:
                exception = {"type":"username_exists","description":"Username already registered in the system"}
                exceptions.append(exception)
            
        if not exceptions:

            user.username = fields["username"]
                    
            user.name = fields["name"]
            user.email = fields["email"]
            user.description = fields["description"]

            db.session.commit()

            response = jsonify({"result":"success", "details": "Changes made successfully"})

            return response

        response = jsonify({"result":"error", "details": exceptions})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()

    return response