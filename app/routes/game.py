from services.config import *

''' Rota: [ game_return_route ]
    descrição: 
'''
@app.route("/game/<int:game_id>")
def game_return_route(game_id):
    pass