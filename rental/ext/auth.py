from flask_simplelogin import SimpleLogin

def verify_login2(user):
    return user.get('username')=='admin' and user.get('password')=='12345'
    
def init_app(app):
    SimpleLogin(app, login_checker=verify_login2)