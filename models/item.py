from sqlalchemy.orm import Mapped

from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.String(255), unique=True, nullable=False)
    description: Mapped[str] = db.Column(db.String(500))
    price: Mapped[float] = db.Column(db.Float, nullable=False)
    store_id: Mapped[int] = db.Column(
        db.Integer, db.ForeignKey("stores.id"), nullable=False
    )

    store = db.relationship("StoreModel", back_populates="items")
    tags = db.relationship("TagModel", back_populates="items", secondary="item_tags")
