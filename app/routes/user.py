''' Importações das configurações '''
from services.config import *
from services.forms import RegisterForm,LoginForm
''' Importações dos formulários '''


''' Rota: [ join_route ]
    descrição: 
'''
@app.route("/join")
def join_route():
    fields = request.form
    return render_template('pages/register.html', form=RegisterForm(fields))

''' Rota: [ join_authenticate_route ]
    descrição: 
'''
@app.route("/join/authenticate", methods = ["POST"])
def join_authenticate_route():
    fields = request.form
    
    if  RegisterForm(fields).validate():
        name = fields['name']
        username = fields['username']
        email = fields['email']
        password = fields['password']
        
        User.join_form(name,username,email,password)

        return redirect(url_for('home_route'))
    else:
        return redirect(url_for('join_route'))

''' Rota: [ login_route ]
    descrição: 
'''
@app.route("/login")
def login_route():
    return render_template('pages/login.html',form= LoginForm(request.form) )

''' Rota: [ login_authenticate_route ]
    descrição: 
'''
@app.route("/login/authenticate", methods = ["POST"])
def login_authenticate_route():
     fields = request.form
     
     if LoginForm(fields).validate():
        username_form = fields["username"]
        password_form = fields["password"]

