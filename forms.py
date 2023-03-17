from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class LoginForm(FlaskForm):
    email = StringField('Email ', [validators.InputRequired()])
    password = PasswordField('Password ', [validators.InputRequired()])