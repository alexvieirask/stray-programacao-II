''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

@app.route("/admin/login", methods=['POST'])
def admin_login_route():
    fields = request.get_json(force=True)  
    username = fields["username"]
    password = fields["password"]

    if User.validate_login(username,password):
        user = db_query_by_username(username)
        
        access_token = create_access_token(identity=username)
        payload = {
            "token": access_token,
            "admin": user.is_admin
        } 

        response =  jsonify({"result":"success", "detalhes": payload}) 
    
    else: 
        response = jsonify({"result": "erro", "detalhes":"usuario ou senha incorreto(s)"})
    return response 


# Em desenvolvimento

'''  
curl -H -X POST --data "{\"username\":\"alex.vieira\",\"password\":\"my-password\"}" http://localhost:5000/admin/login
'''