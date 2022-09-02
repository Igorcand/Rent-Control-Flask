from rental.ext.database import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(180), unique=False, nullable=False)

    def __repr__(self):
        return self.username

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(50), unique=True)
    number = db.Column(db.Integer, unique=False)
    city = db.Column(db.String(50), unique=False)
    state = db.Column(db.String(50), unique=False)
    country = db.Column(db.String(50), unique=False)
    zipcode = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Address %r>' % self.name

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=False, nullable=False)
    payment = db.Column(db.Float, unique=False, nullable=False)
    entry = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    activate = db.Column(db.Boolean, unique=False, nullable=False)

    def __repr__(self):
        return '<Tenant %r>' % self.username

# class Property(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), unique=False, nullable=False)
#     iptu = db.Column(db.Integer, unique=False, nullable=False)
#     value = db.Column(db.Float, unique=False, nullable=False)
#     pendency = db.Column(db.Integer, unique=True, nullable=False)

#     tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'),nullable=False)
#     category = db.relationship('Tenant',backref=db.backref('tenant', lazy=True))

#     address_id = db.Column(db.Integer, db.ForeignKey('address.id'),nullable=False)
#     category = db.relationship('Address',backref=db.backref('address', lazy=True))


#     def __repr__(self):
#         return '<Property %r>' % self.username

