from flask import Blueprint
from .customer.routes import bp as customer
from .address.routes import bp as address
from .tenant.routes import bp as tenant


webui = Blueprint("webui", __name__, template_folder="templates")
webui.register_blueprint(customer)
webui.register_blueprint(address)
webui.register_blueprint(tenant)


def init_app(app):
    app.register_blueprint(webui)