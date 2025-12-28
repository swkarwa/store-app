from sqlalchemy.orm import Mapped

from db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(500), unique=True, nullable=False)
    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic", cascade="all , delete"
    )
    tags = db.relationship(
        "TagModel", back_populates="store", lazy="dynamic", cascade="all , delete"
    )
