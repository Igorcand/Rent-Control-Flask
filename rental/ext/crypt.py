from flask_bcrypt import  Bcrypt

def init_app(app):
    bcrypt = Bcrypt(app)