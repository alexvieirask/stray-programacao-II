from services.config import *
from schemas.user import User
from services.encrypt import *

@app.route("/user/register", methods = ['GET', 'POST'])
def user_register_route():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if name and age and username and email and password:
            user = User(name = name, age = age,
            username = username ,email = email,
            password = encrypt_password(password))
            
            db.session.add(user)
            db.session.commit()            
            
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
