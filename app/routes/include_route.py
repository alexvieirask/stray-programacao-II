''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *
from services.default_datas import default_games, default_users

''' Rota: [ include_route ]
    descrição: 

    Testes:
            1. curl -H \Content-Type:application/json\ -X POST --data "{\"name\":\"Alex Vieira Dias\",\"username\":\"alexvieirasdias\",\"email\":\"alexvieirasdias@gmail.com\",\"password\":\"teste\"}" http://localhost:5000/user/include
            2. curl -H \Content-Type:application/json\ -X POST --data "{\"name\":\"Emanoela Rodrigues Erthal\",\"username\":\"manu_erthal\",\"email\":\"manu@gmail.com\",\"password\":\"manu\"}" http://localhost:5000/user/include
            3. curl -H \Content-Type:application/json\ -X POST --data "{\"title\":\"The test\",\"description\":\"this game...\",\"categorie\":\"aventura\",\"price\":\"2\",\"required_age\":\"0\",\"launch_date\":\"24/01/2005\",\"developer\":\"The Tester\",\"cover\":\"https://images.tcdn.com.br/img/img_prod/691184/teste_213_1_20200528133119.png\"}" http://localhost:5000/game/include
   
    Obs.: Esta rota necessita do JWT no corpo da requisição.
'''
@app.route("/<string:class_type>/include", methods = ["POST"])
def include_route(class_type):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ]  
        datas = request.get_json(force=True)
    
        for type in class_list:    
            if type.__tablename__ == class_type:
                new_data = type(**datas)
                
                db.session.add(new_data)
                db.session.commit()
    
                response = jsonify({"result":"ok", "details": 'Success'})
                return response
        response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    return response

''' Rota: [ default_datas_route ]
    descrição: Rota para inserir os dados padrõoes para teste do sistema.
    
    Testes:
        localhost:5000/default_datas
'''
@app.route("/default_datas")
def default_datas_route():
    try:
        response = jsonify({"result":"ok", "details": 'Default Datas Success!'})
        
        for user in default_users:
            db.session.add(user)
        for game in default_games:
            db.session.add(game)  
       
        db.session.commit()

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    return response