from tests.giftcard import *
from tests.user import *
from tests.game import *
from tests.purchase import *

''' 
User test

create:
print(create_user('Alex Vieira Dias','LiLCrazzyFN', 
'alexvieiradias2019@gmail.com', 'my-password', '60', 
'24/01/2005','Lindo', 'Alex.png'))

or 

print(create_user('e','e', 
'e@gmail.com', 'e-password', '60', 
'24/01/2005','e', 'e.png'))


'''


''' 
Purchase test - make the user have a game

create: 
print(create_purchase(1,1))


verify:
user: User = User.query.get(1).purchases[0]
print(user.game.title) 

'''


''' DEFAULT DATABASE ITEMS

default_games_add()

'''