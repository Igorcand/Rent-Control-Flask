from flask import Blueprint
from .products.routes import bp as product

webui = Blueprint("webui", __name__, template_folder="templates")
webui.register_blueprint(product)


def init_app(app):
    app.register_blueprint(webui)