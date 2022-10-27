from services.config import *
from services.utils import *

''' Rota: [ game_return_route ]
    descrição: Esta rota retorna um jogo em especifico.
'''
@app.route("/game/<int:id>/<string:title>")
def game_return_route(id, title):
    current_game = db_query_by_id(Game,id)
    return jsonify({"result" :current_game.json() })