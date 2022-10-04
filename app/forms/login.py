from wtforms import Form, PasswordField, StringField
from wtforms.validators import Length, InputRequired

class LoginForm(Form):
    username = StringField('Username',[
        InputRequired(), 
        Length(min= 3, max= 20)
    ])
    
    password = PasswordField ('Password',[
        InputRequired(),
        Length(min= 4, max = 64)
    ])