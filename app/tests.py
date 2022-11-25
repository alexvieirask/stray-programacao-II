from services.config import *
from services.utils import *

user = db_query_by_username(User,"alex.vieira") 

games_buyed = sorted(user.purchases)


print(user.giftcards)