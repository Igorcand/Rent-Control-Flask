from flask import Blueprint
from .customer.routes import bp as customer
from .address.routes import bp as address

webui = Blueprint("webui", __name__, template_folder="templates")
webui.register_blueprint(customer)
webui.register_blueprint(address)


def init_app(app):
    app.register_blueprint(webui)