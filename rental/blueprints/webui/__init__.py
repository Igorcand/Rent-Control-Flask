from flask import Blueprint
from .customer.routes import bp as customer
from .address.routes import bp as address
from .tenant.routes import bp as tenant
from .property.routes import bp as property



webui = Blueprint("webui", __name__, template_folder="templates")
webui.register_blueprint(customer)
webui.register_blueprint(address)
webui.register_blueprint(tenant)
webui.register_blueprint(property)


def init_app(app):
    app.register_blueprint(webui)