''' Importações das configurações '''
from services.config import *
from services.utils import *

''' Rota: [ join_route ]
    descrição:
'''
@app.route("/join")
def join_route():
    return render_template('pages/register.html')

''' Rota: [ login_route ]
    descrição: 
'''
@app.route("/login")
def login_route():
    return render_template('pages/login.html')

''' Rota: [ join_authenticate_route ]
    descrição: 

    Testes:
'''
@app.route("/join/auth", methods = ["POST"])
def join_authenticate_route():
    try:
        fields = request.get_json()
        hash_password = generate_password_hash(fields["password"]).decode("utf-8")

        new_user = User(
            name = fields["name"], 
            username = fields["username"], 
            email = fields["email"], 
            password = hash_password
        )    
        
        db.session.add(new_user)
        db.session.commit()

        response = jsonify({"result":"success", "details": new_user.json()})
        
    except Exception as error:
        response = jsonify({"result":"error", "details":str(error)})
    
    return response
  
