from flask_restx import Api, Resource, fields, Namespace, reqparse
from rental.models import  Tenant as TenantModel

from rental.ext.database import db
from flask import request

ns = Namespace(name='tenants', description='Tenants operations')

tenant_model = ns.model('Tenat', 
{
    'id': fields.Integer(description='Tenat ID'),
    'name': fields.String(description='Tenat name'),
    'age': fields.Integer(description='Tenat age'),
    'cpf': fields.Integer(description='Tenat cpf '),
    'phone': fields.Integer(description='Tenat phone '),
    'payment': fields.Float(description='Tenat payment '),
    'entry': fields.Integer(description='Tenat entry'),
    'email': fields.String(description='Tenat entry'),
    'activate': fields.Boolean(description='activate'),
    'user_id': fields.Integer(description='user id'),
})



@ns.route('/')
class Tenant(Resource):
    @ns.marshal_list_with(tenant_model, code=200, envelope='tenants')
    def get(self):
        '''Get all addresses'''
        tenants = TenantModel.query.all()
        return tenants

    @ns.marshal_list_with(tenant_model, code=200, envelope='tenant')
    @ns.expect(tenant_model)
    def post(self):
        data = request.get_json()
        id = data.get('id')
        address = TenantModel.query.filter_by(id=id).first()
        if address:
            ns.abort(404, description=f"This address id '{id}' already exist")
        name = data.get('name')
        age = data.get('age')
        cpf = data.get('cpf')
        phone = data.get('phone')
        payment = data.get('payment')
        entry = data.get('entry')
        email = data.get('email')
        activate = data.get('activate')
        user_id = data.get('user_id')

        tenant = TenantModel(name=name, age=age, cpf=cpf, phone=phone, payment=payment, entry=entry, email=email,activate=activate, user_id=user_id)
        db.session.add(tenant)
        db.session.commit()
        return address

     
@ns.route('/<int:id>/')
class TenantResource(Resource):

    @ns.marshal_with(tenant_model, code=200, envelope='tenant')
    @ns.response(404, 'Todo not found')
    def get(self, id):
        tenant = TenantModel.query.filter_by(id=id).first()
        if tenant:
            return tenant
        ns.abort(404, description=f"This tenant id '{id}' doesen't exist")
        
    
    @ns.marshal_with(tenant_model, code=200, envelope='tenant')
    @ns.expect(tenant_model)
    def put(self,id):

        ''' Update a book'''
        tenant = TenantModel.query.filter_by(id=id).first()
        if tenant:

            data=request.get_json()
            tenant.name=data.get('name')
            tenant.age=data.get('age')
            tenant.cpf=data.get('cpf')
            tenant.phone=data.get('phone')
            tenant.payment=data.get('payment')
            tenant.entry=data.get('entry')
            tenant.email=data.get('email')
            tenant.activate=data.get('activate')
            db.session.commit()
        else:
            data = request.get_json()
            id = data.get('id')
            tenant = TenantModel.query.filter_by(id=id).first()
            if tenant:
                ns.abort(404, description=f"This tenant id '{id}' already exist")
            name = data.get('name')
            age = data.get('age')
            cpf = data.get('cpf')
            phone = data.get('phone')
            payment = data.get('payment')
            entry = data.get('entry')
            email = data.get('email')
            activate = data.get('activate')
            user_id = data.get('user_id')

            tenant = TenantModel(name=name, age=age, cpf=cpf, phone=phone, payment=payment, entry=entry, email=email,activate=activate, user_id=user_id)
            db.session.add(tenant)
            db.session.commit()

        return tenant,200

    @ns.marshal_with(tenant_model, code=200, envelope='tenant')
    def delete(self,id):
        '''Delete a book'''
        tenant = TenantModel.query.filter_by(id=id).first()
        if tenant:
            db.session.delete(tenant)
            db.session.commit()
            return tenant,200
        ns.abort(404, description=f"This tenant ID '{id}' doesen't exist")