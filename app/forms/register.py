from wtforms import Form, PasswordField, StringField, EmailField
from wtforms.validators import Length, InputRequired, EqualTo

class RegisterForm(Form):
    name = StringField('Name',[
        InputRequired(), 
        Length(min= 1, max= 64)
    ])

    username = StringField('Username',[
        InputRequired(), 
        Length(min= 3, max= 20)
    ])
    
    email = EmailField('E-mail',[
        InputRequired(), 
        Length(min= 1, max= 64)
    ])
    
    password = PasswordField ('New Password',[
        InputRequired(),
        Length(min= 4, max = 64)
    ])

    password_confirm = PasswordField('confirm password',[
        EqualTo('password', message= 'Passwords do not match, check again ')
    ])

