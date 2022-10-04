from services.config import *
from services.encrypt import *
from schemas.user import User
from forms.register import RegisterForm
from forms.login import LoginForm


@app.route("/user/register", methods = ['GET', 'POST'])
def user_register_route():
    form_register = RegisterForm(request.form)

    
    if request.method == 'POST' and form_register.validate():
        
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        User.register_form(
            name = name,
            username = username,
            email = email,
            password = password
        )

        return redirect(url_for('initial_route'))
    
    return render_template('register.html', form=form_register , title = 'User Register')

@app.route("/user/login", methods = ['GET', 'POST'])
def user_login_route():
    form_login = LoginForm(request.form)
    
    if request.method == 'POST' and form_login.validate():
        username = request.form['username']
        password = request.form['password']
        
        hash_password = encrypt_password(password)
        
        user = User.query.filter_by(username = username, password = hash_password).first()

        if user != None:
            access_token = create_access_token(identity=username)
            return redirect(url_for('initial_route'))
        else:
            return '<h1> User no exists </h1>'
    
    return render_template('login.html',form=form_login, title = 'User Login' )

@app.route("/user/return_all")
def user_return_route():
    try:
        users = db.session.query(User).all()
        json_users = [ user.json() for user in users ]
        response = jsonify({'result':'ok', 'details': json_users})
    
    except Exception as error:
        response = jsonify({'result':'error', 'details':str(error)})

    return response
