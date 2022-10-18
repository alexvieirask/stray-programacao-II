''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

'''Esquema Screenshot:

atributos:
    id: Integer
    url: Text
    alt: Text
    game_id: Integer <ForeingKey(Game.id)>
'''
class Screenshot(db.Model):
    __tablename__ = 'Screenshot'
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.Text, nullable = False)
    alt = db.Column(db.Text, nullable = False)
    game_id = db.Column(db.Integer,db.ForeignKey('Game.id'))
    
    def json(self):
        return{
            "id": self.id,
            "url": self.url,
            "alt": self.alt,
            "game_id": self.game_id
        }

    def screenshot_add(url:str, alt:str, game_id: int) -> tuple:
        try:
            new_screenshot = Screenshot(
                url = url, 
                alt = alt, 
                game_id = game_id
            ) 

            db_insert(new_screenshot)
            return 200, new_screenshot.json()

        except Exception as error:
            return str(error)        