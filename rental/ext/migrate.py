from flask_migrate import Migrate
from rental.ext.database import db

# Single-database configuration for Flask.
# flask db init
# flask db migrate -m "message"
# flask db upgrade


def init_app(app):
    migrate=Migrate(app, db)
    with app.app_context():
        if db.engine.url.drivername=='sqlite':
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate=Migrate(app, db)