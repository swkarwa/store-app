from sqlalchemy.orm import Mapped

from db import db


class TagItemModel(db.Model):
    __tablename__ = "item_tags"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    item_id: Mapped[int] = db.Column(
        db.Integer, db.ForeignKey("items.id"), nullable=False
    )
    tag_id: Mapped[int] = db.Column(
        db.Integer, db.ForeignKey("tags.id"), nullable=False
    )
