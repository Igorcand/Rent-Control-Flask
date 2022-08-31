from flask import Blueprint
from flask_restx import Api
from .resources import ns as teste
from .resources.users import ns as users
from .resources.users import UserResource, AllUsersResource



restapi = Blueprint('restapi', __name__, url_prefix='/api')
api = Api(restapi, version='1.0',title='Rent Controll API',description='A Rent Controll API',doc = '/docs', default_label='Everything to you control your rents', default = 'Rent', license='license')
api.add_namespace(teste)
api.add_namespace(users)


def init_app(app):
    users.add_resource(AllUsersResource, '/all_user')
    users.add_resource(UserResource, '/<string:username>')

    app.register_blueprint(restapi)