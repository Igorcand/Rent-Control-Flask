from flask_restx import Api, Resource, fields, Namespace, reqparse
from rental.models import  Address as AddressModel

from rental.ext.database import db
from flask import request

ns = Namespace(name='addresses', description='Users operations')

address_model = ns.model('Address', 
{
    'id': fields.Integer(description='User ID'),
    'street': fields.String(description='Street name'),
    'number': fields.Integer(description='Number house'),
    'city': fields.String(description='City name'),
    'state': fields.String(description='State name'),
    'country': fields.String(description='Country name'),
    'zipcode': fields.Integer(description='Zipcode'),
    'user_id': fields.Integer(description='user id'),
})



@ns.route('/')
class Address(Resource):
    @ns.marshal_list_with(address_model, code=200, envelope='addresses')
    def get(self):
        '''Get all addresses'''
        addresses = AddressModel.query.all()
        return addresses

    @ns.marshal_list_with(address_model, code=200, envelope='address')
    @ns.expect(address_model)
    def post(self):
        data = request.get_json()
        id = data.get('id')
        address = AddressModel.query.filter_by(id=id).first()
        if address:
            ns.abort(404, description=f"This address id '{id}' already exist")
        street = data.get('street')
        number = data.get('number')
        city = data.get('city')
        state = data.get('state')
        country = data.get('country')
        zipcode = data.get('zipcode')
        user_id = data.get('user_id')

        address = AddressModel(street=street, number=number, city=city, state=state, country=country, zipcode=zipcode, user_id=user_id)
        db.session.add(address)
        db.session.commit()
        return address

     
@ns.route('/<int:id>/')
class AddressResource(Resource):

    @ns.marshal_with(address_model, code=200, envelope='address')
    @ns.response(404, 'Todo not found')
    def get(self, id):
        address = AddressModel.query.filter_by(id=id).first()
        if address:
            return address
        ns.abort(404, description=f"This address id '{id}' doesen't exist")
        
    
    @ns.marshal_with(address_model, code=200, envelope='address')
    def put(self,id):

        ''' Update a book'''
        address = AddressModel.query.filter_by(id=id).first()
        if address:

            data=request.get_json()
            address.street=data.get('street')
            address.number=data.get('number')
            address.city=data.get('city')
            address.state=data.get('state')
            address.country=data.get('country')
            address.zipcode=data.get('zipcode')


            db.session.commit()
        else:
            data = request.get_json()
            id = data.get('id')
            address = AddressModel.query.filter_by(id=id).first()
            if address:
                ns.abort(404, description=f"This address id '{id}' already exist")
            street = data.get('street')
            number = data.get('number')
            city = data.get('city')
            state = data.get('state')
            country = data.get('country')
            zipcode = data.get('zipcode')
            user_id = data.get('user_id')

            address = AddressModel(street=street, number=number, city=city, state=state, country=country, zipcode=zipcode, user_id=user_id)
            db.session.add(address)
            db.session.commit()

        return address,200

    @ns.marshal_with(address_model, code=200, envelope='address')
    def delete(self,id):
        '''Delete a book'''
        address = AddressModel.query.filter_by(id=id).first()
        if address:
            db.session.delete(address)
            db.session.commit()
            return address,200
        ns.abort(404, description=f"This address ID '{id}' doesen't exist")
   
    