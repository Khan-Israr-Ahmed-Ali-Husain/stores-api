from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import request

from models.item import ItemModel

class Item(Resource):

    @jwt_required()
    def get(self,name):        
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200 
        return {"messsage" : name + " is not available"} , 404

    def post(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return {'message':'An item with this name is already exists'}, 404
        data = ItemModel.parser.parse_args()
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return {"item" : item.json()}, 201
        
    def put(self,name):
        
        data = ItemModel.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:   
            item.store_id = data['store_id']         
            item.price = data['price']
            item.save_to_db()
            return {'message':'Price updated successfully'}, 201
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return {"message" : "Item created successfully" ,
            "item" : item.json()}, 201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db() 
            return {"message": name + " deleted successfully"}
        return {"message": name + " does not exists"}
        
        
class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}        
