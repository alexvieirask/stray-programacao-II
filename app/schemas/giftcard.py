from services.config import *
from services.encrypt import giftcard_generator

''' Giftcard Schema:
atrr:
    id: Integer
    value: Text
    giftcard_code: Text
    available: Boolean <Default value: true>


functions:
    create_giftcard
    set_used_giftcard
    return_all_giftcards
    return_giftcard_by_id                                  

'''

class GiftCard(db.Model):
    __tablename__ = 'GiftCard'
    id = db.Column(db.Integer, primary_key = True)
    value = db.Column(db.Integer)
    giftcard_code = db.Column(db.Text, unique = True)
    available = db.Column(db.Boolean, default= True)


    ''' this function return datas in JSON format '''
    def json(self) -> dict:
        return {
            "id:": self.id,
            "value": self.value,
            "giftcard_code": self.giftcard_code,
            'available': self.available
        }
    
    '''this func'''
    def create_giftcard() -> tuple:
        try:
            CODES_QUERY = db.session.query(GiftCard).all()
            NEW_CODE = giftcard_generator()
            GIFTCARD_CODES = []   
            
            for code in CODES_QUERY:
                GIFTCARD_CODES.append(code.giftcard_code)

            if NEW_CODE in GIFTCARD_CODES:
                NEW_CODE = giftcard_generator()

            else:
                TOKEN_GIFTCARD = GiftCard( value = 50, giftcard_code = NEW_CODE )
                db.session.add(TOKEN_GIFTCARD)
                db.session.commit()     
                return 200, TOKEN_GIFTCARD.json()

        except Exception as error:
            return str(error)

    '''this func'''
    def set_used_giftcard(id) -> tuple:
        try:
            GIFTCARD = GiftCard.query.get(id)
            GIFTCARD.available = False
            db.session.commit()
            return 200, GIFTCARD

        except Exception as error:
            return str(error)

    '''this func'''
    def return_all_giftcards() -> tuple:
        try:
            GIFTCARDS = db.session.query(GiftCard).all()
            json_giftcards = [ giftcard.json() for giftcard in GIFTCARDS ]
            return 200, json_giftcards

        except Exception as error:
            return str(error)

    ''' this func  '''
    def return_giftcard_by_id(id) -> tuple:
        try:
            GIFTCARD = GiftCard.query.get(id)
            return 200, GIFTCARD.json()
            
        except Exception as error:
            return str(error)