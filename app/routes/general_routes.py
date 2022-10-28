''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *
from services.default_datas import default_games, default_users

''' Rota: [ return_all_route ]
    descrição: Esta rota retorna todos os itens de uma determinada tabela da database.

    Testes:
        1. curl localhost:5000/user/return_all
        2. curl localhost:5000/giftcard/return_all
        3. curl localhost:5000/medal/return_all
        4. curl localhost:5000/screenshot/return_all
        5. curl localhost:5000/purchase/return_all

    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/<string:class_type>/return_all")
@jwt_required()
def return_all_route(class_type):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ]

        for type in class_list:
            if type.__tablename__ == class_type:
                datas = db_query_all(type)
                json_datas = [ data.json() for data in datas ]
                response = jsonify({"result":"ok", "details":json_datas})
                return response
            response = jsonify({"result":"error", "details":"Bad Request"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})

    return response

''' Rota: [ return_data_route ]
    descrição: Esta Rota retorna um item especifico de uma determinada tabela.

    Testes:
        1. curl localhost:5000/user/1
        2. curl localhost:5000/game/1
        3. curl localhost:5000/giftcard/1
        4. curl localhost:5000/medal/1
        5. curl localhost:5000/screenshot/1
        6. curl localhost:5000/purchase/1

    Obs.: Esta rota necessita do JWT no corpo da requisição. 
'''
@app.route("/<string:class_type>/<int:id>")
@jwt_required()
def return_data_route(class_type , id):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ]

        for type in class_list:
            if type.__tablename__ == class_type:
                data = db_query_by_id(type,id)
                response = jsonify({"result":"ok", "details":data.json()})
                return response
            response = jsonify({"result":"error", "details":"Bad Request"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})

    return response

''' Rota: [ include_route ]
    descrição:

    Testes:
        1. curl -H "Content-Type:application/json" -X POST --data "{\"name\":\"Alex Vieira Dias\",\"username\":\"alexvieirasdias\",\"email\":\"alexvieirasdias@gmail.com\",\"password\":\"teste\"}" http://localhost:5000/user/include
        2. curl -H "Content-Type:application/json" -X POST --data "{\"name\":\"Emanoela Rodrigues Erthal\",\"username\":\"manu_erthal\",\"email\":\"manu@gmail.com\",\"password\":\"manu\"}" http://localhost:5000/user/include
        3. curl -H "Content-Type:application/json" -X POST --data "{\"title\":\"The test\",\"description\":\"this game...\",\"categorie\":\"aventura\",\"price\":\"2\",\"required_age\":\"0\",\"launch_date\":\"24/01/2005\",\"developer\":\"The Tester\",\"cover\":\"https://images.tcdn.com.br/img/img_prod/691184/teste_213_1_20200528133119.png\"}" http://localhost:5000/game/include

    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/<string:class_type>/include", methods = ["POST"])
@jwt_required()
def include_route(class_type):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ]
        datas = request.get_json()

        for type in class_list:
            if type.__tablename__ == class_type:
                new_data = type(**datas)

                db.session.add(new_data)
                db.session.commit()

                response = jsonify({"result":"ok", "details":"Success"})
                return response
        response = jsonify({"result":"error", "details":"Bad Request"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()

    return response

''' Rota: [ delete_route ]
    descrição: Esta rota é responsável por deletar um item de uma determinada tabela da database.

    Testes:
        1. curl localhost:5000/user/delete/1
        2. curl localhost:5000/game/delete/1
        3. curl localhost:5000/giftcard/delete/1
        4. curl localhost:5000/medal/delete/1
        5. curl localhost:5000/screenshot/delete/1
        6. curl localhost:5000/purchase/delete/1

    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/<string:class_type>/delete/<int:id>")
@jwt_required()
def delete_route(class_type:str, id:int):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ]

        for type in class_list:
            if type.__tablename__ == class_type:
                data = db_query_by_id(type,id)

                db.session.delete(data)
                db.session.commit()

                response = jsonify({"result":"ok", "details":"Success"})
                return response

            response = jsonify({"result":"error", "details":"Bad Request"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})

    finally:
        db.session.close()

    return response

''' Rota: [ default_datas_route ]
    descrição: Rota para inserir os dados padrões para teste do sistema.

    Testes:
        1. curl localhost:5000/default_data
'''
@app.route("/default_data")
def default_datas_route():
    try:
        db_add_many_objects(default_games)
        db_add_many_objects(default_users)
        response = jsonify({"result":"ok", "details":"Default data has been entered successfully."})
        
    except IntegrityError:
        response = jsonify({"result":"error", "details":"The default data has already been entered before."})
    
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()
        
    return response