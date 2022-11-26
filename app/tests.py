from services.config import *
from services.utils import *

game = db_query_by_id(Game,1) 
screenshot = Screenshot(url="teste.com", alt="teste.alt", game_id=1)
db.session.add(screenshot)
db.session.commit()


print(game.screenshots) 



