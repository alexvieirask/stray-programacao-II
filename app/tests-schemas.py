
''' Default values for tests '''
from services.default_datas import default_games, default_users

''' Schemas imports '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard
from schemas.medal import Medal
from schemas.screenshot import Screenshot
from schemas.purchase import Purchase

''' Database start '''
from services.database__init__ import *

def default_users_add(users:list) -> int:
    try:
        for user in users:
            db.session.add(user)
        db.session.commit()
        return 200
    
    except Exception as error:
        return str(error)

def default_games_add(games:list) -> int:
    try:
        for game in games:
            db.session.add(game)
        db.session.commit()
        return 200
    
    except Exception as error:
        return str(error)

def default_values():
    try:
        default_users_add(default_users)
        default_games_add(default_games)
        return 200
    
    except Exception as error:
        return str(error)