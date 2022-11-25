from services.config import *
from services.utils import *

''' Rota: [ request_giftcard_route ]
    descrição: Esta rota cria um giftcard para poder ser utilizado.

    Testes:
        1. curl localhost:5000/giftcard/30 -H "Authorization:Bearer "TOKEN_JWT"
        2. curl localhost:5000/giftcard/50 -H "Authorization:Bearer "TOKEN_JWT"
        3. curl localhost:5000/giftcard/100 -H "Authorization:Bearer "TOKEN_JWT"
    
    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/giftcard/<int:value>")
@jwt_required()
def request_giftcard_route(value):
    try:
        GIFTCARD_VALUES = ( 30, 50, 100, 200 )

        if value in GIFTCARD_VALUES:
            value_in_cents = value * 100

            username = get_jwt_identity()
            user = db_query_by_username(User,username) 

            token_giftcard =  GiftCard.giftcard_generator()

            new_giftcard = GiftCard(value= value_in_cents, giftcard_code= token_giftcard, user_id = user.id)
            
            db.session.add(new_giftcard)
            db.session.commit()
            
            response = jsonify({"result":"ok", "details": new_giftcard.json()})
        
        else: 
            response = jsonify({"result":"error", "details": "Unexpected giftcard value."})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()

    return response


''' Rota: [ use_giftcard_route ]
    descrição: Esta rota adiciona o valor do giftcard para o usuário que utilizou.

    Testes:
        1. curl localhost:5000/giftcard/use/GIFTCARD_CODE -H "Authorization:Bearer "TOKEN_JWT"
    
    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/giftcard/use/<string:token>")
@jwt_required()
def use_giftcard_route(token):
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username) 

        giftcard =  GiftCard.query.filter_by(giftcard_code = token).first()

        if giftcard and giftcard.available:
            user.wallet += giftcard.value
            GiftCard.giftcard_used(giftcard)
            db.session.commit()
         
            response = jsonify({"result":"ok", "details": user.json() })
        else:
           response = jsonify({"result":"error", "details": "Giftcard does not exist or used." })
       
    except Exception as error:
        response = jsonify({"result":"ok", "details":"refresh"})
    
    finally:
        db.session.close()

    return response