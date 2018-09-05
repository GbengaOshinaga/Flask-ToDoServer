from marshmallow import Schema, fields

class TodoSchema(Schema):
    id = fields.String(dump_only=True)
    day = fields.String(required=True)
    todo = fields.String(required=True)