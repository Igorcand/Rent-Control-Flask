from rental.ext.database import db
from rental.models import UserModel



def init_app(app):
    @app.cli.command()
    def create_db():
        '''Este comando inicializa o banco de dados'''
        db.create_all()

    @app.cli.command()
    def populate_db():
        """Populate db with sample data"""
        data = [
            UserModel(name="igor", username='igor01',email="igor@email.com", password="1234"),
            UserModel(name="vitor", username='vitor01',email="vitor@email.com", password="1234"),
            UserModel(name="breno", username='breno01',email="breno@email.com", password="1234"),
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return UserModel.query.all()