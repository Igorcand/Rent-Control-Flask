from flask import Blueprint

from .products.routes import home

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=home)
#bp.add_url_rule(
#    "/product/<product_id>", view_func=product, endpoint="productview"
#)


def init_app(app):
    app.register_blueprint(bp)