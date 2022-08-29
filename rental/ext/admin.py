from flask_admin import Admin 

admin = Admin()

def init_app(app):
    admin.name = app.config.get('ADMIN_NAME', 'Rental Controller')
    admin.init_app(app)