from sqlalchemy.orm import Mapped

from db import db


class UserModel(db.Model):
    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    user_name: Mapped[str] = db.Column(db.String(80), unique=True, nullable=False)
    password: Mapped[str] = db.Column(db.String(80), nullable=False)
