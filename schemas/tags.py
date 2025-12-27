from marshmallow import fields, Schema

from schemas import PlainTagSchema, PlainStoreSchema, PlainItemSchema


class TagSchema(PlainTagSchema):
    store = fields.Nested(PlainStoreSchema, dump_only=True)
    items = fields.Nested(PlainItemSchema, many=True, dump_only=True)

class TagUpdateSchema(Schema):
    name = fields.Str()
    store_id = fields.Integer()
