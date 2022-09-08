from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError

from flask_wtf import FlaskForm, Form

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])