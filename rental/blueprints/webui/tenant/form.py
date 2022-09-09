from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, IntegerField, TextAreaField, DecimalField
from flask_wtf import Form, FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired

class TenantForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    age = IntegerField('Age', [validators.DataRequired()])
    cpf = IntegerField('CPF', [validators.DataRequired()])
    phone = IntegerField('Phone', [validators.DataRequired()])
    payment = DecimalField('Payment', [validators.DataRequired()])
    entry = IntegerField('Entry', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired()])
    activate = BooleanField('Activate', [validators.DataRequired()])