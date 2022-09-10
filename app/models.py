"""This is the models module.

This module defines the entities and prepare them to Object-relational mapping.
Also uses marshmallow_sqlalchemy to dump the objects to JSON when needed
"""

from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, SQLAlchemyAutoSchema


db = SQLAlchemy()

card_groups = db.Table(
    "card_groups",
    db.Column("card_id", db.Integer, db.ForeignKey("card.id")),
    db.Column("group_id", db.Integer, db.ForeignKey("groups.id")),
)


class Card(db.Model):
    __tablename__ = "card"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    hint = db.Column(db.String())
    groups = db.relationship(
        "Group", secondary=card_groups, backref=db.backref("groups")
    )

    def __repr__(self):
        # return '<id {}>'.format(self.id)
        return "<Card -> {}>".format(self.title)


class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())

    def __repr__(self):
        # return '<id {}>'.format(self.id)
        return "<Group -> {}>".format(self.title)


class CardSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Card
        include_relationships = True
        load_instance = True


class GroupSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        include_fk = True
        load_instance = True
