from wtforms import Form, PasswordField, StringField, EmailField, SubmitField, validators

class UserForm(Form):
    name = StringField('Name',[
        validators.input_required(), 
        validators.length(min= 1, max= 64)])

    username = StringField('Username',[
        validators.input_required(), 
        validators.length(min= 1, max= 20)])
    
    email = EmailField('E-mail',[
        validators.input_required(), 
        validators.length(min= 1, max= 35)])
    
    password = PasswordField ('New Password',[
        validators.data_required(),
        validators.equal_to('confirm', message= "Passwords don't match")
    ])
    
    confirm = PasswordField('Repeat Password ')