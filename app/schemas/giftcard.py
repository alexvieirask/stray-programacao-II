''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

'''Esquema Giftcard:

atributos:
    id: Integer
    value: Text
    giftcard_code: Text
    available: Boolean <Default value: true>
    user_id: Integer <ForeingKey(User.id)> 
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
    
    def create_giftcard(user_buyer_id: int) -> tuple:
        try:
            codes_query = db_query_all(GiftCard)
            new_code = giftcard_generator()
            giftcard_codes = []   
            
            for code in codes_query:
                giftcard_codes.append(code.giftcard_code)

            if new_code in giftcard_codes:
                new_code = giftcard_generator()
            else:
                new_giftcard = GiftCard( 
                    value = 50, 
                    giftcard_code = 
                    new_code, 
                    user_id = user_buyer_id 
                )

                db_insert(new_giftcard)     
                return 200, new_giftcard.json()

        except Exception as error:
            return str(error)

    def set_used_giftcard(id:int) -> tuple:
        try:
            giftcard = db_query_by_id(GiftCard,id)
            giftcard.available = False
        
            db.session.commit()
            return 200, giftcard.json()

        except Exception as error:
            return str(error)

def giftcard_generator() -> str:
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    quantity_digit = 12
    
    response = ''.join(random.sample(characters, quantity_digit))
    return response