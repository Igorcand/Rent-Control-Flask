from rental.ext.database import db

#One to many
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)
    #    name of class that we want conect | name of actual class
    addresses = db.relationship('Address', backref='user')
    tenants = db.relationship('Tenant', backref='user')
    properties = db.relationship('Property', backref='user')



    def __repr__(self):
        return self.username

class Address(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(50), unique=False)
    number = db.Column(db.Integer, unique=False)
    city = db.Column(db.String(50), unique=False)
    state = db.Column(db.String(50), unique=False)
    country = db.Column(db.String(50), unique=False)
    zipcode = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    address_user = db.relationship('Property', backref='address')

    def __repr__(self):
        return '<Address %r>' % self.name

class Tenant(db.Model):
    __tablename__ = 'tenants'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=False, nullable=False)
    payment = db.Column(db.Float, unique=False, nullable=False)
    entry = db.Column(db.Integer, unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    activate = db.Column(db.Boolean, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    tenant_user = db.relationship('Property', backref='tenant')

    def __repr__(self):
        return '<Tenant %r>' % self.username

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    iptu = db.Column(db.Integer, unique=False, nullable=False)
    value = db.Column(db.Float, unique=False, nullable=False)
    pendency = db.Column(db.Boolean, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'))



    def __repr__(self):
        return '<Property %r>' % self.username