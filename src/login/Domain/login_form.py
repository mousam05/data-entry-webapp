from wtforms import Form, BooleanField, StringField, PasswordField, validators


class login_form(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    role = StringField('Role', [validators.Length(min=4, max=25)])
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
