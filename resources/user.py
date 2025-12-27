from os import abort

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

from db import db
from models import UserModel
from schemas.common import PlainUserSchema

blp = Blueprint('users', __name__, description='operations on users')


@blp.route('/user/<int:user_id>')
class User(MethodView):

    @blp.response(200 , PlainUserSchema)
    def get(self, user_id):
        return UserModel.query.get_or_404(user_id)

    @blp.response(204, description='user deleted')
    @blp.alt_response(404, description='user does not exists')
    def delete(self , user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'msg' : 'user deleted'}


@blp.route('/register')
class RegisterUser(MethodView):

    @blp.arguments(PlainUserSchema)
    @blp.response(201 , PlainUserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.user_name == user_data['user_name']).first():
            return abort(409, message='user already exists')

        user = UserModel(
            user_name=user_data['user_name'],
            password = pbkdf2_sha256.hash(user_data['password'])
        )

        db.session.add(user)
        db.session.commit()
        return user

@blp.route("/login")
class LoginUser(MethodView):

    @blp.arguments(PlainUserSchema)
    def post(self , user_data):
        user = UserModel.query.filter(UserModel.user_name == user_data['user_name']).first()
        if user and pbkdf2_sha256.verify(user_data['password'] , user.password):
            access_token = create_access_token(identity=str(user.id))
            return {'token' : access_token} , 200
        return abort(400 , message='invalid creds')

