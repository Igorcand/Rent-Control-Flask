from flask_restx import Api, Resource, fields, Namespace, reqparse
from rental.models import  Property as PropertyModel

from rental.ext.database import db
from flask import request

ns = Namespace(name='properties', description='Property operations')

property_model = ns.model('Property', 
{
    'id': fields.Integer(description='Property ID'),
    'name': fields.String(description='Property name'),
    'iptu': fields.Integer(description='Property age'),
    'value': fields.Integer(description='Property cpf '),
    'phone': fields.Integer(description='Property phone '),
    'pendancy': fields.Float(description='Property payment '),
    'address_id': fields.Integer(description='Address id'),
    'tenant_id': fields.String(description='Tenat id'),
    'user_id': fields.Integer(description='user id'),
})



@ns.route('/')
class Property(Resource):
    @ns.marshal_list_with(property_model, code=200, envelope='properties')
    def get(self):
        '''Get all addresses'''
        property = PropertyModel.query.all()
        return property

    @ns.marshal_list_with(property_model, code=200, envelope='property')
    @ns.expect(property_model)
    def post(self):
        data = request.get_json()
        id = data.get('id')
        property = PropertyModel.query.filter_by(id=id).first()
        if property:
            ns.abort(404, description=f"This property id '{id}' already exist")
        name = data.get('name')
        iptu = data.get('age')
        value = data.get('cpf')
        pendancy = data.get('phone')
        address_id = data.get('payment')
        tenant_id = data.get('entry')
        user_id = data.get('user_id')

        property = PropertyModel(name=name, iptu=iptu, value=value, pendancy=pendancy, address_id=address_id, entenant_idtry=tenant_id, user_id=user_id)
        db.session.add(property)
        db.session.commit()
        return property

     
@ns.route('/<int:id>/')
class PropertyResource(Resource):

    @ns.marshal_with(property_model, code=200, envelope='property')
    @ns.response(404, 'Todo not found')
    def get(self, id):
        property = PropertyModel.query.filter_by(id=id).first()
        if property:
            return property
        ns.abort(404, description=f"This property id '{id}' doesen't exist")
        
    
    @ns.marshal_with(property_model, code=200, envelope='property')
    @ns.expect(property_model)
    def put(self,id):

        ''' Update a book'''
        property = PropertyModel.query.filter_by(id=id).first()
        if property:

            data=request.get_json()
            property.name=data.get('name')
            property.age=data.get('iptu')
            property.cpf=data.get('value')
            property.phone=data.get('pendancy')
            property.payment=data.get('address_id')
            property.entry=data.get('tenant_id')
            db.session.commit()
        else:
            data = request.get_json()
            id = data.get('id')
            property = PropertyModel.query.filter_by(id=id).first()
            if property:
                ns.abort(404, description=f"This property id '{id}' already exist")
            name = data.get('name')
            iptu = data.get('age')
            value = data.get('cpf')
            pendancy = data.get('phone')
            address_id = data.get('payment')
            tenant_id = data.get('entry')
            user_id = data.get('user_id')

            property = PropertyModel(name=name, iptu=iptu, value=value, pendancy=pendancy, address_id=address_id, entenant_idtry=tenant_id, user_id=user_id)
            db.session.add(property)
            db.session.commit()

        return property,200

    @ns.marshal_with(property_model, code=200, envelope='property')
    def delete(self,id):
        '''Delete a book'''
        property = PropertyModel.query.filter_by(id=id).first()
        if property:
            db.session.delete(property)
            db.session.commit()
            return property,200
        ns.abort(404, description=f"This property ID '{id}' doesen't exist")