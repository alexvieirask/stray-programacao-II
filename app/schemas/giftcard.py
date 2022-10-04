from services.config import *
from services.encrypt import giftcard_generator

''' Giftcard Schema:

atributes:
    id: Integer
    value: Text
    giftcard_code: Text
    available: Boolean <Default value: true>
'''

class GiftCard(db.Model):
    __tablename__ = 'GiftCard'
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer, nullable = False)
    giftcard_code = db.Column(db.Text, nullable = False, unique = True)
    available = db.Column(db.Boolean, default= True)

    def json(self) -> dict:
        return {
            "id:": self.id,
            "value": self.value,
            "giftcard_code": self.giftcard_code,
            'available': self.available
        }
    
    def create_giftcard() -> tuple:
        try:
            codes_query = db.session.query(GiftCard).all()
            new_code = giftcard_generator()
            giftcard_codes = []   
            
            for code in codes_query:
                giftcard_codes.append(code.giftcard_code)

            if new_code in giftcard_codes:
                new_code = giftcard_generator()
            else:
                giftcard = GiftCard( value = 50, giftcard_code = new_code )
                db.session.add(giftcard)
                db.session.commit()     
                return 200, giftcard.json()

        except Exception as error:
            return str(error)

    def set_used_giftcard(id) -> tuple:
        try:
            giftcard = GiftCard.query.get(id)
            giftcard.available = False
            db.session.commit()
            return 200, giftcard.json()

        except Exception as error:
            return str(error)

        try:
            GIFTCARD = GiftCard.query.get(id)
            return 200, GIFTCARD.json()
            
        except Exception as error:
            return str(error)