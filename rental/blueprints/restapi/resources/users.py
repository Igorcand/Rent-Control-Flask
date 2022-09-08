from flask_restx import Api, Resource, fields, Namespace, reqparse
from rental.models import  User as UserModel
from rental.ext.database import db
from flask import request

ns = Namespace(name='users', description='Users operations')

user_model = ns.model('User', 
{
    'id': fields.Integer(description='User ID'),
    'name': fields.String(description='User name'),
    'username': fields.String(description='Username'),
    'email': fields.String(description='User email'),
    'password': fields.Integer(description='User password'),
})



@ns.route('/')
class Users(Resource):
    @ns.marshal_list_with(user_model, code=200, envelope='users')
    def get(self):
        '''Get all users'''
        users = UserModel.query.all()
        return users

    @ns.marshal_list_with(user_model, code=200, envelope='user')
    @ns.expect(user_model)
    def post(self):
        data = request.get_json()
        
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = UserModel(name=name, username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return user

     
@ns.route('/<string:username>/')
class UserResource(Resource):

    @ns.marshal_with(user_model, code=200, envelope='user')
    @ns.response(404, 'Todo not found')
    def get(self, username):
        user = UserModel.query.filter_by(username=username).first()
        if user:
            return user
        ns.abort(404, description=f"This username '{username}' doesen't exist")
        
    
    @ns.marshal_with(user_model, code=200, envelope='user')
    def put(self,username):

        ''' Update a book'''
        user = UserModel.query.filter_by(username=username).first()
        if user:

            data=request.get_json()
            print(f'data = {data}')

            user.name=data.get('name')
            user.username=data.get('username')
            user.email=data.get('email')
            user.password=data.get('password')

            db.session.commit()
        else:
            data = request.get_json()
        
            name = data.get('name')
            username = data.get('username')
            verity_user = UserModel.query.filter_by(username=username).first()
            if verity_user:
                ns.abort(404, description=f"This username '{username}' already exist")

            email = data.get('email')
            verity_user = UserModel.query.filter_by(email=email).first()
            if verity_user:
                ns.abort(404, description=f"This email '{email}' already exist")

            password = data.get('password')
            user = UserModel(name=name, username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()

        return user,200

    @ns.marshal_with(user_model, code=200, envelope='user')
    def delete(self,username):
        '''Delete a book'''
        user = UserModel.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return user,200
        ns.abort(404, description=f"This username '{username}' doesen't exist")
   
    