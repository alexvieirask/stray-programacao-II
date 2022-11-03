from services.config import *
from services.utils import *

''' Rota: [ game_return_route ]
    descrição: Esta rota retorna um jogo em especifico.

    Testes:
        1. curl localhost:5000/game/1/Celeste
'''
@app.route("/game/<int:id>/<string:title>")
def game_return_route(id, title):
    current_game = db_query_by_id(Game,id)
    return jsonify({"result":"ok", "details": current_game.json() })

''' Rota: [ games_return_route ]
    descrição: Esta rota retorna todos os jogos cadastrados na database.

    Testes:
        1. curl localhost:5000/game/return_all
'''
@app.route("/game/return_all")
def games_return_route():
    try:
        datas = db_query_all(Game)
        json_datas = [ data.json() for data in datas ]
        response = jsonify({"result":"ok", "details":json_datas})
        return response

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})

    return response

''' Rota: [ game_purchase_route ]
    descrição: Esta é a rota de compra de um jogo.

    Testes:
        curl localhost:5000/game/purchase/1 -H "Authorization:Bearer "TOKEN_JWT"
        curl localhost:5000/game/purchase/2 -H "Authorization:Bearer "TOKEN_JWT"
        curl localhost:5000/game/purchase/3 -H "Authorization:Bearer "TOKEN_JWT"
        curl localhost:5000/game/purchase/4 -H "Authorization:Bearer "TOKEN_JWT"
        curl localhost:5000/game/purchase/5 -H "Authorization:Bearer "TOKEN_JWT"
    
     Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/game/purchase/<int:game_id>")
@jwt_required()
def game_purchase_route(game_id):
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username) 
        game = db_query_by_id(Game,game_id)

        if game:
            if game.price <= user.wallet: 
                new_purchase = Purchase(user_buyer_id= user.id, game_buyed_id= game_id)
                
                user.wallet -= game.price
                
                db.session.add(new_purchase)
                db.session.commit()
                
                response = jsonify({"result":"ok", "details": new_purchase.json()})

            else:
                response = jsonify({"result":"error", "details": "User does not have enough money."})
        
        else:
            response = jsonify({"result":"error", "details": "this game id does not exist."})


    except IntegrityError:
        response = jsonify({"result":"error", "details": "The user already owns this game."})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()

    return response