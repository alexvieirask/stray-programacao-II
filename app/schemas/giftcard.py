''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Esquema: [ Giftcard ]
    descrição: Esquema de Giftcard utilizado no sistema.
'''
class GiftCard(db.Model):
    __tablename__ = 'Giftcard'
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable = False)
    giftcard_code = db.Column(db.Text, nullable = False, unique = True)
    available = db.Column(db.Boolean, default= True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    def json(self) -> dict:
        return {
            "id:": self.id,
            "value": self.value,
            "giftcard_code": self.giftcard_code,
            "available": self.available,
            "user_id" : self.user_id 
        }
    
    def giftcard_generator() -> str:
        LETTERS_AND_NUMBERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        token_generate = ''

        for item in range(3):
            TOKEN = ''.join(random.sample(LETTERS_AND_NUMBERS,4))
            token_generate += TOKEN 
            if item < 2:
                token_generate += '-' 
        
        return(token_generate)
    
    def giftcard_used(giftcard):
        try:
            giftcard.available = False
            db.session.commit()
            response = jsonify({"result":"ok", "details": "Success"})

        except Exception as error:
            response = jsonify({"result":"error", "details":str(error)})
        
        finally:
            db.session.close()
        
        return response