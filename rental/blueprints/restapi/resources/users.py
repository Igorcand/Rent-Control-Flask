from flask_restx import Api, Resource, fields, Namespace, reqparse
from rental.models import  UserModel

ns = Namespace(name='users', description='Users operations')

user_doc = ns.model('User', 
{
    'id': fields.Integer(description='User ID'),
    'name': fields.String(description='User name'),
    'username': fields.String(description='Username'),
    'email': fields.String(description='User email'),
    'password': fields.Integer(description='User password'),
})

class AllUsersResource(Resource):

    @ns.doc('list_user')
    @ns.marshal_with(user_doc)
    def get(self):
        user = UserModel.find_all()
        print(user)
        return [UserModel( name=x.name, username=x.username, email=x.email, password=x.password).json() for x in user] 
     
# INSERT INTO user_model (name, username, email, password) VALUES ("igor", "igor01", "igor@email.com", "1234")
class UserResource(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True, help="This field cannot be left blank")
    #parser.add_argument("username", type=str, required=True, help="This field cannot be left blank")
    parser.add_argument("email", type=str, required=True, help="This field cannot be left blank")
    parser.add_argument("password", type=str, required=True, help="This field cannot be left blank")


    @ns.doc('list_user')
    @ns.marshal_with(user_doc)
    def get(self, username):
        user = UserModel.find_by_username(username)
        print(user)
        if user:
            return user.json() 
        return {'message': 'Username name not found'}, 404 
    
    @ns.doc('add_user')
    @ns.marshal_with(user_doc)
    def post(self, username):
        data = UserResource.parser.parse_args()
        username = data['username']
        email = data['email']

        if UserModel.find_by_username(username):
            return (
                {"Message": f"An user with username '{username}' already exists"}
            )
        
        if UserModel.find_by_email(email):
            return (
                {"Message": f"An user with email '{email}' already exists"}
            )
        user = UserModel.query.all()
        return [UserModel( name=x.name, username=x.username, email=x.email).json() for x in user] 
    