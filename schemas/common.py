from marshmallow import Schema, fields

class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True) # should receive from server, cannot send it
    user_name  = fields.Str(required=True)
    password = fields.Str(required=True , load_only=True) # can only send from client side, never to receive it