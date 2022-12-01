''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *
from services.default_datas import default_games, default_users, default_screenshots

''' Rota: [ return_all_route ]
    descrição: Esta rota retorna todos os itens de uma determinada tabela da database.

    Testes:
        1. curl localhost:5000/user/return_all -H "Authorization: Bearer [TOKEN]"
        2. curl localhost:5000/giftcard/return_all -H "Authorization: Bearer [TOKEN]"
        3. curl localhost:5000/medal/return_all -H "Authorization: Bearer [TOKEN]"
        4. curl localhost:5000/screenshot/return_all -H "Authorization: Bearer [TOKEN]"
        5. curl localhost:5000/purchase/return_all -H "Authorization: Bearer [TOKEN]"

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
        1. curl localhost:5000/user/1 -H "Authorization: Bearer [TOKEN]"
        2. curl localhost:5000/game/1 -H "Authorization: Bearer [TOKEN]"
        3. curl localhost:5000/giftcard/1 -H "Authorization: Bearer [TOKEN]"
        4. curl localhost:5000/medal/1 -H "Authorization: Bearer [TOKEN]"
        5. curl localhost:5000/screenshot/1 -H "Authorization: Bearer [TOKEN]"
        6. curl localhost:5000/purchase/1 -H "Authorization: Bearer [TOKEN]"

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
        1. curl -H "Content-Type:application/json" -H "Authorization: Bearer [TOKEN]" -X POST --data "{\"name\":\"Alex Vieira Dias\",\"username\":\"alexvieirasdias\",\"email\":\"alexvieirasdias@gmail.com\",\"password\":\"teste\"}" http://localhost:5000/user/include
        2. curl -H "Content-Type:application/json" -H "Authorization: Bearer [TOKEN]" -X POST --data "{\"name\":\"Emanoela Rodrigues Erthal\",\"username\":\"manu_erthal\",\"email\":\"manu@gmail.com\",\"password\":\"manu\"}" http://localhost:5000/user/include
        3. curl -H "Content-Type:application/json" -H "Authorization: Bearer [TOKEN]" -X POST --data "{\"title\":\"The test\",\"description\":\"this game...\",\"categorie\":\"aventura\",\"price\":\"2\",\"required_age\":\"0\",\"launch_date\":\"24/01/2005\",\"developer\":\"The Tester\",\"cover\":\"https://images.tcdn.com.br/img/img_prod/691184/teste_213_1_20200528133119.png\"}" http://localhost:5000/game/include

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
        1. curl localhost:5000/user/delete/1 "Authorization: Bearer [TOKEN]"
        2. curl localhost:5000/game/delete/1 "Authorization: Bearer [TOKEN]"
        3. curl localhost:5000/giftcard/delete/1 "Authorization: Bearer [TOKEN]"
        4. curl localhost:5000/medal/delete/1 "Authorization: Bearer [TOKEN]"
        5. curl localhost:5000/screenshot/delete/1 "Authorization: Bearer [TOKEN]"
        6. curl localhost:5000/purchase/delete/1 "Authorization: Bearer [TOKEN]"

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
                
                if data:
                    db.session.delete(data)
                    db.session.commit()
                    response = jsonify({"result":"success", "details":"{} successfully deleted".format(type.__tablename__)})
                else:
                    response = jsonify({"result":"error", "details":"{} not found".format(type.__tablename__)})

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
        db_add_many_objects(default_screenshots)
        
        response = jsonify({"result":"ok", "details":"Default data has been entered successfully."})
        
    except IntegrityError:
        response = jsonify({"result":"error", "details":"The default data has already been entered before."})
    
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()
        
    return response


''' Rota: [ send_money_route ]
    descrição: Esta rota envia dinheiro para um usuário em especifico.

    Testes:
        1. curl localhost:5000/1/send/100 -H "Authorization: Bearer [TOKEN]"
        3. curl localhost:5000/1/send/1000 -H "Authorization: Bearer [TOKEN]"
        2. curl localhost:5000/2/send/10000 -H "Authorization: Bearer [TOKEN]"

    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/<int:id>/send/<int:value>")
@jwt_required()
def send_money_route(id:int,value:int):
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username) 

        if user.is_admin:
            user_to_send = db_query_by_id(User, id)

            if user_to_send and value>0:
                wallet_in_cents = value * 100
                user_to_send.wallet += wallet_in_cents
                db.session.commit()

                response = jsonify({"result":"success", "details":"Money sent to {}".format(user_to_send.username)})

            else:
                response = jsonify({"result":"error", "details":"User not found or invalid value" })
        else:
            response = jsonify({"result":"error", "details":"You are not an admin"})

    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})

    finally:
        db.session.close()

    return response


''' Rota: [ save_image_route ]
    descrição: Esta rota é responsável por salvar a imagem de perfil de um usuário em especifico.

    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/save_image", methods = ["POST"])
@jwt_required()
def save_image_route():
    try:
        username = get_jwt_identity()
        user = db_query_by_username(User,username)
        FILE = request.files['input-picture-profile'] 

        if FILE:

            VALID_EXTENSIONS = ['JPEG', 'PNG', 'JPG']
            PREFIX_ARCHIVE = "user"
            DEFAULT_EXTENSION  = ".JPEG"

            EXTENSION_ARCHIVE = FILE.filename.split(".")
            LEN_ARCHIVE_NAME_SPLIT = len(EXTENSION_ARCHIVE)
            EXTENSION_ARCHIVE = EXTENSION_ARCHIVE[LEN_ARCHIVE_NAME_SPLIT-1].upper()
            
            missing_folders = ["src","static","img","uploads","users"]

            PATH_IMG = PATH_FROM_MAIN_FOLDER(missing_folders) + PREFIX_ARCHIVE + str(user.id) + DEFAULT_EXTENSION
            
            if EXTENSION_ARCHIVE in VALID_EXTENSIONS:
                FILE.save(PATH_IMG)
                
                response = jsonify({"result":"success", "details": PATH_IMG})
                
                return response
            
            response = jsonify({"result":"error", "details": 'This image is not valid.'})
        else:
            response = jsonify({"result":"success", "details": "No image changes"})
    
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response