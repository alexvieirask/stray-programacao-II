''' Importação dos esquemas '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard
from schemas.medal import Medal
from schemas.screenshot import Screenshot
from schemas.purchase import Purchase

''' Inicializando o banco de dados '''
from services.database__init__ import *