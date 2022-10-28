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