from wtforms import BooleanField, StringField, PasswordField, validators , ValidationError, IntegerField, TextAreaField, DecimalField
from flask_wtf import Form, FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired

class AddressForm(FlaskForm):
    street = StringField('Street', [validators.DataRequired()])
    number = IntegerField('Number', [validators.DataRequired()])
    city = StringField('City', [validators.DataRequired()])
    state = StringField('State', [validators.DataRequired()])
    country = StringField('Country', [validators.DataRequired()])
    zipcode = IntegerField('Zipcode', [validators.DataRequired()])