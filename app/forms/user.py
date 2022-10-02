from wtforms import Form, PasswordField, validators, StringField

class UserForm(Form):
    name = StringField('Name',[validators.input_required(), validators.Length(min= 1, max= 25)])
    username = StringField('Username',[validators.input_required(), validators.Length(min= 1, max= 25)])
    email = StringField('E-mail',[validators.input_required(), validators.Length(min= 1, max= 35)])
    password =  PasswordField ('New Password',[
        validators.DataRequired(),
        validators.EqualTo('Password Confirm', message= "Passwords don't match")
    ])
    password_confirm = PasswordField('Password Repeat')
