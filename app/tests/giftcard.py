from services.config import *
from services.encrypt import giftcard_generator
from schemas.giftcard import  GiftCard 

''' Giftcard Schema:
atrr:
    id: Integer
    value: Text
    giftcard_code: Text
    available: Boolean <Default value: true>


functions:
    create_giftcard
    set_used_giftcard
    return_giftcard_by_id
                                                 
'''
                    
                    

'''this func'''
def create_giftcard():
    try:
        CODES_QUERY = db.session.query(GiftCard).all()
        NEW_CODE = giftcard_generator()
        GIFTCARD_CODES = []   
        
        for code in CODES_QUERY:
            GIFTCARD_CODES.append(code.giftcard_code)

        if NEW_CODE in GIFTCARD_CODES:
            create_giftcard()
        else:
            TOKEN_GIFTCARD = GiftCard( value = 50, giftcard_code = NEW_CODE )
            db.session.add(TOKEN_GIFTCARD)
            db.session.commit()     
            return 200

    except Exception as error:
        return str(error)

'''this func'''
def set_used_giftcard(id):
    try:
        GIFTCARD = GiftCard.query.get(id)
        GIFTCARD.available = False
        db.session.commit()
        print(f'GIFTCARD COM O ID {id} foi utilizado')
        return 200

    except Exception as error:
        return str(error)

''' this func  '''
def return_giftcard_by_id(id):
    try:
        GIFTCARD = GiftCard.query.get(id)
        print(GIFTCARD.json())
        return 200


    except Exception as error:
        return str(error)