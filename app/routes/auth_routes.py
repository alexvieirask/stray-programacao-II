''' Importação das configurações e serviços '''
from services.config import *
from services.utils import *

''' Rota: [ login_authenticate_route ]
    descrição: Esta rota realiza a autenticação do usuário e retorna o Token JWT.

    Testes:
        1. curl -H "Content-Type:application/json" -X POST --data "{\"username\":\"alex.vieira\",\"password\":\"my-password\"}" http://localhost:5000/login/auth
        2. curl -H "Content-Type:application/json" -X POST --data "{\"username\":\"emanoela.erthal\",\"password\":\"my-password2\"}" http://localhost:5000/login/auth

    Algumas rotas protegidas:
        1. curl localhost:5000/user/return_all -H "Authorization:Bearer [TOKEN]"
        2. curl localhost:5000/giftcard/return_all -H "Authorization:Bearer [TOKEN]"
'''
@app.route("/login/auth", methods=['POST'])
def login_authenticate_route():
    try:
        fields = request.get_json()

        if User.validate_login(fields["username"],fields["password"]):
            access_token = create_access_token(identity = fields["username"])

            response =  jsonify({"result":"ok", "details":access_token})
        else:
            response = jsonify({"result": "error", "details":"Incorrect username or password."})
            
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response


''' Rota: [ join_authenticate_route ]
    descrição: Esta rota realiza a autenticação para a criação de um novo usuário.

    Testes:
        1. curl -H "Content-Type:application/json" -X POST --data "{\"name\":\"Alex Vieira Dias\",\"username\":\"alexvieirasdias\",\"email\":\"alexvieirasdias@gmail.com\",\"password\":\"teste\"}" http://localhost:5000/join/auth
'''
@app.route("/join/auth", methods = ["POST"])
def join_authenticate_route():
    try:
        fields = request.get_json()
        username_exists = db_query_by_username(User, fields["username"])
        email_exists = db_query_by_email(User, fields["email"])

        if not username_exists and not email_exists:
                hash_password = generate_password_hash(fields["password"]).decode("UTF-8")

                new_user = User (
                    name = fields["name"],
                    username = fields["username"],
                    email = fields["email"],
                    password = hash_password
                )

                db.session.add(new_user)
                db.session.commit()

                response = jsonify({"result":"ok", "details":"User registered successfully."})
          
        else:
            response = jsonify({"result":"error", "details":"Username already registered in the system.", "exists": {"email": str(email_exists), "username":str(username_exists)}})
            
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    finally:
        db.session.close()

    return response