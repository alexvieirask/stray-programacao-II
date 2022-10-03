from services.config import *
from schemas.giftcard import GiftCard

@app.route('/giftcard/return_all')
def return_giftcard_route():
    try:
        giftcards = db.session.query(GiftCard).all()
        json_giftcards = [ giftcard.json() for giftcard in giftcards ]
        response = jsonify({'result':'ok', 'details': json_giftcards})
    
    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response