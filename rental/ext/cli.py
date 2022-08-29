from rental.ext.database import db

def init_app(app):
    @app.cli.command()
    def create_db():
        '''Este comando inicializa o banco de dados'''
        db.create_all()