from services.config import *
from schemas.purchase import Purchase


''' this func '''
def create_purchase(game_id: int, user_id: int):
    try:
        PURCHASE = Purchase(user_id = user_id, game_id = game_id ) 
        db.session.add(PURCHASE)
        db.session.commit()
        return 200

    except Exception as error:
        return str(error)
