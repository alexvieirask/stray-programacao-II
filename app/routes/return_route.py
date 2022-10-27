''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Rota: [ return_all_route ]
    descrição: Esta rota retorna todos os itens de uma determinada tabela da daatbase.

    Testes:
        1. curl localhost:5000/user/return_all 
        2. curl localhost:5000/game/return_all
        3. curl localhost:5000/giftcard/return_all
        4. curl localhost:5000/medal/return_all 
        5. curl localhost:5000/screenshot/return_all
        6. curl localhost:5000/purchase/return_all
    
    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/<string:class_type>/return_all")
def return_all_route(class_type):
    try: 
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ] 
        
        for type in class_list:    
            if type.__tablename__ == class_type:
                datas = db_query_all(type)
                json_datas = [ data.json() for data in datas ]
                response = jsonify({"result":"ok", "details": json_datas})
                return response
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response

''' Rota: [ return_data_route ]
    descrição: Esta Rota retorna um item especifico de uma determinada tabela.

    Testes:
        1. curl localhost:5000/user/return/1
        2. curl localhost:5000/game/return/1
        3. curl localhost:5000/giftcard/return/1
        4. curl localhost:5000/medal/return/1
        5. curl localhost:5000/screenshot/return/1
        6. curl localhost:5000/purchase/return/1
    
    Obs.: Esta rota necessita do JWT no corpo da requisição. 
'''
@app.route("/<string:class_type>/return/<int:id>")
@jwt_required()
def return_data_route(class_type , id):
    try: 
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ] 

        for type in class_list:    
            if type.__tablename__ == class_type:
                data = db_query_by_id(type,id)
                response = jsonify({"result":"ok", "details": data.json()})
                return response   
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response