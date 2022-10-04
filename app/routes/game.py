
from services.config import *
from schemas.game import Game

@app.route("/game/return_all")
def game_return_route():
    try:
        games = db.session.query(Game).all()
        json_games = [ user.json() for user in games ]
        response = jsonify({'result':'ok', 'details': json_games})
    
    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})

    return response
