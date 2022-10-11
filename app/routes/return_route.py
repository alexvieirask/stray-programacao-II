''' Config import '''
from services.config import *

''' Schemas imports '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard
from schemas.medal import Medal
from schemas.screenshot import Screenshot
from schemas.purchase import Purchase


''' Route tests

1. curl localhost:5000/user/return_all 
2. curl localhost:5000/game/return_all
3. curl localhost:5000/giftcard/return_all

'''
@app.route("/<string:class_type>/return_all")
def return_all_route(class_type):
    try: 
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ] 
        
        for type in class_list:    
            if type.__tablename__ == class_type:
                datas = db.session.query(type).all()
                json_datas = [ data.json() for data in datas ]
                response = jsonify({"result":"ok", "details": json_datas})
                return response
        
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response

''' Route tests

4. curl localhost:5000/user/return/1
5. curl localhost:5000/game/return/1
6. curl localhost:5000/giftcard/return/1

'''
@app.route("/<string:class_type>/return/<int:id>")
def return_data_route(class_type , id):
    try: 
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ] 

        for type in class_list:    
            if type.__tablename__ == class_type:
                data = db.session.query(type).get_or_404(id)
                response = jsonify({"result":"ok", "details": data.json()})
                return response
                
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response