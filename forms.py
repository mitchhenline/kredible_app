from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, DateField, TextAreaField

class LoginForm(FlaskForm):
    email = StringField('Email ', [validators.InputRequired()])
    password = PasswordField('Password ', [validators.InputRequired()])

class RequestMeetingForm(FlaskForm):
    prospect_email = StringField('Prospect Email ', [validators.InputRequired()])
    notes = StringField('What the email will say:', [validators.InputRequired()])