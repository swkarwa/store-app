from marshmallow import Schema , fields

from schemas import PlainTagSchema
from schemas.common import PlainItemSchema, PlainStoreSchema

class ItemInStoreSchema(PlainItemSchema):
    tags = fields.Nested(PlainTagSchema, many=True, dump_only=True)

class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema, dump_only=True)
    tags = fields.Nested(PlainTagSchema , many=True , dump_only=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()