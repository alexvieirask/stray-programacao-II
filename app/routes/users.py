from services.config import *
from schemas.user import User

''' this route contains the list of all users
    that are registered in the system. 
'''
@app.route("/user/list")
def user_list():
    users = db.session.query(User).all()
    json_users = [ user.json() for user in users ]
    response = jsonify(json_users)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
