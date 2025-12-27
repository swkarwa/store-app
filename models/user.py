from db import db

class UserModel(db.Model):

    id = db.Column(db.Integer , primary_key = True)
    user_name = db.Column(db.String(80) , unique=True , nullable=False)
    password = db.Column(db.String(80) , nullable=False)
