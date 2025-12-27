from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from models.store import StoreModel
from models.tag import TagModel
from schemas.common import PlainTagSchema
from schemas.tags import TagUpdateSchema, TagSchema

blp = Blueprint('tags', __name__, description='operation on tag resources')


@blp.route("/store/<int:store_id>/tag")
class TagsForStore(MethodView):

    @blp.arguments(PlainTagSchema)
    @blp.response(201, TagSchema)
    @blp.alt_response(404, description='resource not found')
    def post(self, tag_data, store_id):
        store = StoreModel.query.get_or_404(store_id)
        if store.tags.filter(TagModel.name == tag_data['name']).first():
            abort(400, message='tag already exists')

        tag = TagModel(**tag_data)
        tag.store_id = store_id
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return tag


@blp.route('/tag/<int:tag_id>')
class Tag(MethodView):

    @blp.response(200, TagSchema)
    @blp.alt_response(404, description='tag does not exist')
    def get(self, tag_id):
        return TagModel.query.get_or_404(tag_id)

    @blp.arguments(TagUpdateSchema)
    @blp.response(200, TagSchema)
    def put(self, tag_data, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        tag.name = tag_data['name']
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return tag

    @blp.response(204, description='tag deleted')
    @blp.alt_response(404, description='tag not found')
    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)
        try:
            db.session.delete(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))


@blp.route('/tags')
class TagList(MethodView):

    @blp.response(200, TagSchema(many=True))
    def get(self):
        return TagModel.query.all()


@blp.route('/item/<int:item_id>/tag/<int:tag_id>')
class ItemTagLink(MethodView):

    @blp.response(200, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        if item.store_id != tag.store_id:
            abort(400, message='linking tag from different store')

        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return tag

    @blp.response(200, TagSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return tag

