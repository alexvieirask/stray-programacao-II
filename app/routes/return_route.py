''' Config import '''
from services.config import *

''' Schemas imports '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard

''' Route tests

1. curl localhost:5000/user/return_all 
2. curl localhost:5000/game/return_all
3. curl localhost:5000/giftcard/return_all

4. curl localhost:5000/user/return/1
5. curl localhost:5000/game/return/1
6. curl localhost:5000/giftcard/return/1

'''

@app.route("/<string:class_type>/return_all")
def return_all_route(class_type):
    try: 
        response = None
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard ] 
 
        for type in class_list:    
            if type.__tablename__ == class_type:
                datas = db.session.query(type).all()
                json_datas = [ data.json() for data in datas ]
                response = jsonify({"result":"ok", "details": json_datas})
                break
        
        if response == None:
            response = jsonify({"result":"error", "details": "Bad Request"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response

@app.route("/<string:class_type>/return/<int:id>")
def return_data_route(class_type , id):
    try: 
        response = None
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard ] 

        for type in class_list:    
            if type.__tablename__ == class_type:
                data = db.session.query(type).get(id)
                
                if data is not None:
                    response = jsonify({"result":"ok", "details": data.json()})
                else:
                    response = jsonify({"result":"error", "details": "ID error!"})
                break

        if response == None:
            response = jsonify({"result":"error", "details": "Bad Request"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response