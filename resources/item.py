from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel, StoreModel
from schemas.items import ItemInStoreSchema, ItemSchema, ItemUpdateSchema

blp = Blueprint("item", __name__, description="operation on item resource")


@blp.route("/item/<int:item_id>")
class ItemOperation(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        return ItemModel.query.get_or_404(item_id)

    @jwt_required()
    @blp.response(204, description="item deleted")
    @blp.alt_response(404, description="item not found")
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        try:
            db.session.delete(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))

    @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema, description="item updated")
    @blp.alt_response(404, description="item not found")
    def put(self, item_data, item_id):
        item = ItemModel.query.get_or_404(item_id)
        for key, value in item_data.items():
            setattr(item, key, value)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return item


@blp.route("/store/<int:store_id>/items")
class ItemsFromStore(MethodView):
    @blp.response(200, ItemInStoreSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.items.all()


@blp.route("/items")
class Items(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()


@blp.route("/item")
class Item(MethodView):
    @jwt_required()
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema, description="item created")
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return item
