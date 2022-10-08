''' Config import '''
from services.config import *

''' Schemas imports '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard


'''Route Tests - don't working

1. curl -d '{"name":"TaldoTeste","username":"taldoteste","email":"taldoteste@gmail.com","password":"my-password"}' -X POST -H "Content-Type:application/json" localhost:5000/user/include


'''

@app.route("/<string:class_type>/include", methods = ['POST'])
def include_route(class_type):
    try:
        datas = request.get_json()
        class_type = class_type.title()
        
        if class_type == "User":
            new_data = User(**datas)
            db.session.add(new_data)
            db.session.commit()
            
            response = jsonify({"result":"ok", "details": 'Success'})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})

    return response