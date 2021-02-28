import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel 

        
class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',
        type=str,
        required=True,
        help='username is required'
        )
        parser.add_argument('password',
        type=str,
        required=True,
        help='password is required'
        )
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message" : "User "+ data['username'] + " already exists, try different name"} , 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message" : "User "+ data['username'] + " created successfully"}, 201

    
