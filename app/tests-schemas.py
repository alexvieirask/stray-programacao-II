
from services.default_datas import GAMES, USERS
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard
from schemas.purchase import Purchase
from schemas.screenshot import Screenshot
from schemas.medal import Medal

''' Here you can take the class tests '''

''' User Schema  '''
User.create_user
User.delete_user
User.default_users_add
User.return_user_by_id  
User.return_all_users
User.return_all_purchases_user

''' Game Schema '''
Game.create_game
Game.set_unavailable_game
Game.default_games_add
Game.return_all_games
Game.return_game_by_id

''' Purchase Schema '''
Purchase.create_purchase
Purchase.return_all_purchases

''' Giftcard Schema '''
GiftCard.create_giftcard
GiftCard.set_used_giftcard
GiftCard.return_all_giftcards
GiftCard.return_giftcard_by_id

''' Screenshot Schema '''
Screenshot.screenshot_add
Screenshot.screenshot_delete


''' Make Tests '''

from services.database__init__ import *
def default_values():
    try:
        User.default_users_add(USERS)
        Game.default_games_add(GAMES)
        return 200
    
    except Exception as error:
        return str(error)