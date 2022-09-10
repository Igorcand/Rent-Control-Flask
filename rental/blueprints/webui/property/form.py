from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, IntegerField, TextAreaField, DecimalField
from flask_wtf import Form, FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired

class PropertyForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    iptu = IntegerField('IPTU', [validators.DataRequired()])
    value = DecimalField('Value', [validators.DataRequired()])
    pendency = BooleanField('Pendency')