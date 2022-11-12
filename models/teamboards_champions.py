from flask import Blueprint, request
from sqlalchemy.sql.dml import Insert
from init import db, ma

from marshmallow import fields

test_bp = Blueprint('test', __name__, url_prefix='/test/')

association_table = db.Table(
    "teamboard_champions",
    # db.Model.metadata,
    db.Column("teamboard_id", db.ForeignKey("teamboards.id"), primary_key=True),
    db.Column("champion_name", db.ForeignKey("champions.name"), primary_key=True)
)

association_table_trt_champ = db.Table(
    "trait_champions",
    # db.Base.metadata,
    db.Column("trait_name", db.ForeignKey("traits.name"), primary_key=True),
    db.Column("champion_name", db.ForeignKey("champions.name"), primary_key=True)
)

association_table_champ_items = db.Table(
    "champion_items",
    # db.Base.metadata,
    db.Column("champion_name", db.ForeignKey("champions.name"), primary_key=True),
    db.Column("item_name", db.ForeignKey("items.name"), primary_key=True)
)

class Champion(db.Model):
    __tablename__ = 'champions'

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    ability = db.Column(db.Text, nullable=False)
    suggested_items = db.Column(db.Text)
    origin_id = db.Column(db.String, db.ForeignKey('origins.name'))
    trait_id = db.Column(db.String, db.ForeignKey('traits.name'))
    items_id = db.Column(db.String, db.ForeignKey('items.name'))

    teamboards = db.relationship('Teamboard', secondary=association_table, back_populates="champions")
    traits = db.relationship('Trait', secondary=association_table_trt_champ, back_populates="champions")
    items = db.relationship('Item', secondary=association_table_champ_items, back_populates="champions")

    origin = db.relationship('Origin', back_populates='champions')
    
class ChampionSchema(ma.Schema):
    origin = fields.Nested('OriginSchema', only=['name'])
    traits = fields.List(fields.Nested('TraitSchema'))
    items = fields.List(fields.Nested('ItemSchema'))

    class Meta:
        fields = ('name', 'cost', 'ability', 'suggested_items', 'origin', 'traits', 'items')
        order_by = 'cost'
        ordered = True

class Teamboard(db.Model):
    __tablename__ = 'teamboards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.Text)

    user_id = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    champions = db.relationship(
        'Champion', secondary=association_table, back_populates='teamboards'
    )

class TeamboardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username'])
    champions = fields.List(fields.Nested('ChampionSchema', only=['name', 'origin', 'traits']))

    class Meta:
        fields = ('id', 'title', 'description', 'champions', 'user')
        ordered = True


class Trait(db.Model):
    __tablename__ = 'traits'

    name = db.Column(db.String(30), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    breakpoints = db.Column(db.String(35))

    champions = db.relationship("Champion", secondary=association_table_trt_champ, back_populates="traits")

class TraitSchema(ma.Schema):

    class Meta:
        fields = ('name', 'description', 'breakpoints')
        ordered = True


class Item(db.Model):
    __tablename__ = 'items'

    name = db.Column(db.String(30), primary_key=True)
    item_bonus = db.Column(db.Text, nullable=False)
    stats = db.Column(db.String(50))

    champions = db.relationship("Champion", secondary=association_table_champ_items, back_populates="items")

class ItemSchema(ma.Schema):

    class Meta:
        fields = ('name', 'item_bonus', 'stats')
        ordered = True