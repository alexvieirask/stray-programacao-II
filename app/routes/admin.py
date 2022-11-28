from services.config import *
from services.utils import *

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
