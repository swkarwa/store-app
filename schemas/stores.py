from marshmallow import Schema, fields
from schemas.common import PlainItemSchema, PlainStoreSchema, PlainTagSchema

class StoreSchema(PlainStoreSchema):
    items = fields.Nested(PlainItemSchema, many=True, dump_only=True)
    tags = fields.Nested(PlainTagSchema , many=True , dump_only=True)