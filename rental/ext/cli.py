from rental.ext.database import db
from rental.models import User as UserModel
from rental.models import Address as AddressModel
from rental.models import Tenant as TenantModel
from rental.models import Property as PropertyModel





def init_app(app):
    @app.cli.command()
    def create_db():
        '''Este comando inicializa o banco de dados'''
        db.create_all()

    @app.cli.command()
    def populate_user_db():
        """Populate db with sample data"""
        data = [
            UserModel(name="igor", username='igor01',email="igor@email.com", password="1234"),
            UserModel(name="vitor", username='vitor01',email="vitor@email.com", password="1234"),
            UserModel(name="breno", username='breno01',email="breno@email.com", password="1234"),
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return UserModel.query.all()
    
    @app.cli.command()
    def populate_address_db():
        """Populate db with sample data"""
        data = [
            AddressModel(street="Rua Azul", number='1353',city="sarzedo", state="Minas", country='Brasil', zipcode='23523',user_id=1),
            AddressModel(street="Rua Vermelha", number='983',city="ibirite", state="são paulo", country='Brasil', zipcode='3411',user_id=1),
            AddressModel(street="Rua arthur", number='15923',city="barreiro", state="Minas", country='Brasil', zipcode='23421',user_id=2),
            AddressModel(street="Rua Maria Joana", number='9083',city="brumadinho", state="Minas", country='Brasil', zipcode='29821',user_id=3),
            
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return AddressModel.query.all()
    
    @app.cli.command()
    def populate_tenant_db():
        """Populate db with sample data"""
        data = [
            TenantModel(name="João", age=31,cpf=12345678910, phone=3190908080, payment=1200.00, entry=7, email='joao@email.com', activate=True, user_id=1),
            TenantModel(name="Marcos", age=19,cpf=1234836910, phone=31977708080, payment=2000.00, entry=3, email='marcos@email.com', activate=True, user_id=1),
            TenantModel(name="Marina", age=54,cpf=12322678910, phone=3192208080, payment=2200.00, entry=4, email='Marina@email.com', activate=True, user_id=2),
            TenantModel(name="Pedro", age=19,cpf=55345678910, phone=5590908080, payment=1900.00, entry=1, email='pedro@email.com', activate=True, user_id=2),
            TenantModel(name="Lidia", age=25,cpf=99345678910, phone=230908080, payment=1500.00, entry=2, email='lidia@email.com', activate=False, user_id=3),
            
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return TenantModel.query.all()

    @app.cli.command()
    def populate_property_db():
        """Populate db with sample data"""
        data = [
            PropertyModel(name="Galpão", iptu=310,value=1000000, pendency=False, address_id=1, tenant_id=1,user_id=1),
            PropertyModel(name="Loja", iptu=550,value=500000, pendency=True, address_id=2, tenant_id=2,user_id=1),
            PropertyModel(name="Casa", iptu=410,value=300000, pendency=False, address_id=3, tenant_id=3,user_id=2),
            PropertyModel(name="Predio", iptu=980,value=800000, pendency=False, address_id=4, tenant_id=4,user_id=3),
            PropertyModel(name="Kitnet", iptu=270,value=50000, pendency=False, address_id=1, tenant_id=5,user_id=3),

            
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return TenantModel.query.all()

    @app.cli.command()
    def populate_test_db():
        """Populate db with sample data"""
        data = [
            PropertyModel(name="Galpão", iptu=310,value=1000000, pendency=False, address_id=1, tenant_id=1,user_id=9),

            
        ]
        db.session.bulk_save_objects(data)
        db.session.commit()
        return TenantModel.query.all()