from flask import Blueprint
from flask_restx import Api
from .resources import ns as ns1

bp = Blueprint('restapi', __name__, url_prefix='/api')
api = Api(bp, version='1.0',title='Rent Controll API',description='A Rent Controll API',doc = '/docs', default_label='Everything to you control your rents', default = 'Rent', license='license')
api.add_namespace(ns1)

def init_app(app):
    app.register_blueprint(bp)