from services.config import *
from services.utils import *

user = db_query_by_id(User,2) 
game = db_query_by_id(Game,1) 

datas = user.purchases


json_datas = [ index.game for index in datas ]
print(json_datas)
#print(user.purchases[0].game.json())
