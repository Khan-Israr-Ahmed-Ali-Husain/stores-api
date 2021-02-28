from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from security import authenticate, identity
from flask_jwt import JWT, jwt_required
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # telling sqlalchemy about database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'

api = Api(app)


jwt = JWT(app, authenticate, identity) # it creates an end point /auth  , we need to pass the credentials, it will return the JWT token which can be used as an identity

api.add_resource(Store,'/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')



if __name__=='__main__':
    from db import db

    db.init_app(app)
    app.run(port = 5000, debug=True)
