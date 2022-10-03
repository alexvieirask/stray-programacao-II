from services.config import *
from services.encrypt import *
from schemas.user import User
from forms.user import UserForm

@app.route("/user/register", methods = ['GET', 'POST'])
def user_register_route():
    form = UserForm(request.form)

    if request.method == 'POST':

        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        hash_password = encrypt_password(password)

        new_user = User(
            name = name, 
            username = username ,
            email = email,
            password = hash_password
        )
        
        db.session.add(new_user)
        db.session.commit()            
            
        return redirect(url_for('initial_route'))
    return render_template('register.html', form= form , title = 'User Register')



@app.route("/user/return_all")
def user_return_route():
    try:
        users = db.session.query(User).all()
        json_users = [ user.json() for user in users ]
        response = jsonify({'result':'ok', 'details': json_users})
    
    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})

    return response



@app.route("/user/login")
def user_login_route():
    return render_template('login.html')
