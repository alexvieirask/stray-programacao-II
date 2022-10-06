
from services.config import *
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard

''' Route tests

1. curl localhost:5000/user/return_all 
2. curl localhost:5000/game/return_all
3. curl localhost:5000/giftcard/return_all

4. curl localhost:5000/user/1
5. curl localhost:5000/game/1
6. curl localhost:5000/giftcard/1

'''

@app.route("/<string:class_type>/return_all")
def return_all_route(class_type):
    try: 
        class_type = class_type.title()
        TYPES_STRING = [ "User", "Game", "Giftcard"] 
        TYPES_CLASS = [ User, Game, GiftCard ] 

        ''' Verifica se a rota requisitada é válida '''
        if class_type in TYPES_STRING:
            index = -1 
            for type in TYPES_STRING:    
                index += 1    
                if type == class_type:
                    class_type = TYPES_CLASS[index]
                    break
            
            ''' Query dinâmica '''
            datas = db.session.query(class_type).all()
            json_datas = [ data.json() for data in datas ]
            response = jsonify({"result":"ok", "details": json_datas})
       
        else:
            response = jsonify({"result":"error", "details": "Bad Request"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response


@app.route("/<string:class_type>/<int:id>")
def return_data_route(class_type , id):
    try: 
        class_type = class_type.title()
        TYPES_STRING = [ "User", "Game", "Giftcard"] 
        TYPES_CLASS = [ User, Game, GiftCard ] 

        ''' Verifica se a rota requisitada é válida '''
        if class_type in TYPES_STRING:
            index = -1 
            for type in TYPES_STRING:    
                index += 1    
                if type == class_type:
                    class_type = TYPES_CLASS[index]
                    break
    
            ''' Query dinâmica '''            
            json_data = db.session.query(class_type).get(id).json()
            response = jsonify({"result":"ok", "details": json_data})
        
        else:
            response = jsonify({"result":"error", "details": "Bad Request"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response