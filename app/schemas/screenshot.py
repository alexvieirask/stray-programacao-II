''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Esquema: [ Screenshot ]
    descrição: 
'''
class Screenshot(db.Model):
    __tablename__ = 'Screenshot'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text, nullable = False)
    alt = db.Column(db.Text, nullable = False)
    game_id = db.Column(db.Integer,db.ForeignKey('Game.id'))
    
    def json(self) -> dict:
        return{
            "id": self.id,
            "url": self.url,
            "alt": self.alt,
            "game_id": self.game_id
        }