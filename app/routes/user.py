from services.config import *
from schemas.user import User

@app.route("/user/register", methods = ['GET', 'POST'])
def user_register_route():
    if request.method == 'POST':
        
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if name and username and email and password:
            
            hash_password = bcrypt.generate_password_hash(password)

            new_user = User(name = name, 
                            username = username ,
                            email = email,
                            password = hash_password)
            
            
            db.session.add(new_user)
            db.session.commit()            
            flash('Usuário Registrado')
        
        return redirect(url_for('initial_route'))
    return render_template('register.html')



@app.route("/user/return_all")
def user_return_route():
    try:
        USERS = db.session.query(User).all()
        json_users = [ user.json() for user in USERS ]
        response = jsonify({'result':'ok', 'details': json_users})
    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})
    
    return response



@app.route("/user/login")
def user_login_route():
    return render_template('login.html')
