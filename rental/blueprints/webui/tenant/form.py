from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, IntegerField, TextAreaField, DecimalField
from flask_wtf import Form, FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired

class TenantForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    age = IntegerField('Age', [validators.DataRequired()])
    cpf = IntegerField('CPF', [validators.DataRequired(), validators.Length(min=11, max=11)])
    phone = IntegerField('Phone', [validators.DataRequired(), validators.Length(min=9, max=14)])
    payment = DecimalField('Payment', [validators.DataRequired()])
    entry = IntegerField('Entry', [validators.DataRequired()])
    expiration = IntegerField('Expiration', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    activate = BooleanField('Activate', [validators.DataRequired()])