from marshmallow import fields
from schemas import ma

class UserSchema(ma.Schema):
    id = fields.Integer(required=False) # id is autogenerated
    username = fields.String(required=True)
    password = fields.String(required=True)
    role = fields.String(required=True)

# Create instances of the schema
user_input_schema = UserSchema()
user_output_schema = UserSchema(exclude=["password"])
user_login_schema = UserSchema(only=["username", "password"])
users_schema = UserSchema(many=True, exclude=["password"])