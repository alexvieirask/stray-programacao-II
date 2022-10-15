''' Config import '''
from services.config import *

''' Schemas imports '''
from schemas.user import User
from schemas.game import Game
from schemas.giftcard import GiftCard
from schemas.medal import Medal
from schemas.screenshot import Screenshot
from schemas.purchase import Purchase

''' Route Test

1. curl localhost:5000/user/delete/1
2. curl localhost:5000/game/delete/1
3. curl localhost:5000/giftcard/delete/1
4. curl localhost:5000/medal/delete/1
5. curl localhost:5000/screenshot/delete/1
6. curl localhost:5000/purchase/delete/1

'''
@app.route("/<string:class_type>/delete/<int:id>")
def delete_route(class_type:str, id:int):
    try:
        class_type = class_type.title()
        class_list = [ User, Game, GiftCard, Medal, Screenshot, Purchase ] 

        for type in class_list:    
            if type.__tablename__ == class_type:
                data = db.session.query(type).get_or_404(id)
                db.session.delete(data)
                db.session.commit()
                response = jsonify({"result":"ok", "details": "Sucess"})
                return response
                
            response = jsonify({"result":"error", "details": "Bad Request [Class Invalid]"})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response

@app.route("/drop_database")
def drop_database_route():
    try:
        db.drop_all()
        response = jsonify({"result":"ok", "details": "Drop database Success! Obs: Reload back-end."})

    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response