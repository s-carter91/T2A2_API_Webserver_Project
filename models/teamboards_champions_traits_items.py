from marshmallow import fields
from init import db, ma

# Champion, Teamboard, Trait and Item are placed in the one python file as I was unable to import association tables into other python files

# The association table joining teamboards and champions
association_table = db.Table(
    'teamboard_champions',
    db.Column('teamboard_id', db.ForeignKey('teamboards.id'), primary_key=True),
    db.Column('champion_name', db.ForeignKey('champions.name'), primary_key=True)
)

# The association table joining traits and champions
association_table_trt_champ = db.Table(
    'trait_champions',
    db.Column('trait_name', db.ForeignKey('traits.name'), primary_key=True),
    db.Column('champion_name', db.ForeignKey('champions.name'), primary_key=True)
)

# The association table joining champions and items
association_table_champ_items = db.Table(
    'champion_items',
    db.Column('champion_name', db.ForeignKey('champions.name'), primary_key=True),
    db.Column('item_name', db.ForeignKey('items.name'), primary_key=True)
)

class Champion(db.Model):
    __tablename__ = 'champions'

    # Columns included in the champion table
    name = db.Column(db.String(30), primary_key=True)
    cost = db.Column(db.Integer, nullable=False)
    ability = db.Column(db.Text, nullable=False)
    origin_id = db.Column(db.String, db.ForeignKey('origins.name'))
    trait_id = db.Column(db.String, db.ForeignKey('traits.name'))
    items_id = db.Column(db.String, db.ForeignKey('items.name'))

    # Many-to-many relationships of the champions table
    teamboards = db.relationship('Teamboard', secondary=association_table, back_populates='champions')
    traits = db.relationship('Trait', secondary=association_table_trt_champ, back_populates='champions')
    items = db.relationship('Item', secondary=association_table_champ_items, back_populates='champions')

    # Many-to-one relationships of the champions table
    origin = db.relationship('Origin', back_populates='champions')
    
class ChampionSchema(ma.Schema):
    origin = fields.Nested('OriginSchema', only=['name', 'description'])
    traits = fields.List(fields.Nested('TraitSchema', only=['name', 'description']))
    items = fields.List(fields.Nested('ItemSchema'))

    class Meta:
        # Displayed all attributs relating to the champion and ordering by cost
        fields = ('name', 'cost', 'ability', 'suggested_items', 'origin', 'traits', 'items')
        order_by = 'cost'
        ordered = True

class Teamboard(db.Model):
    __tablename__ = 'teamboards'

    # Columns included in the teamboards table
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False, unique=True)
    description = db.Column(db.Text)
    user_id = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    # Many-to-many relationship of the teamboards table
    champions = db.relationship('Champion', secondary=association_table, back_populates='teamboards')

    # Many-to-one relationship of the teamboards table
    user = db.relationship('User', back_populates='teamboards')

class TeamboardSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['username'])
    champions = fields.List(fields.Nested('ChampionSchema', only=['name', 'origin', 'traits']))

    class Meta:
        fields = ('id', 'title', 'description', 'user', 'champions')
        ordered = True


class Trait(db.Model):
    __tablename__ = 'traits'

    # Columns included in the teamboards table
    name = db.Column(db.String(30), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    breakpoints = db.Column(db.String(35), nullable=False)

    # One-to-many relationship of the traits table
    champions = db.relationship('Champion', secondary=association_table_trt_champ, back_populates='traits')

class TraitSchema(ma.Schema):

    class Meta:
        fields = ('name', 'description', 'breakpoints')
        ordered = True


class Item(db.Model):
    __tablename__ = 'items'

    # Columns included in the items table
    name = db.Column(db.String(30), primary_key=True)
    item_bonus = db.Column(db.Text, nullable=False)
    stats = db.Column(db.String(50), nullable=False)

    # Many-to-many relationship of the items table
    champions = db.relationship('Champion', secondary=association_table_champ_items, back_populates='items')

class ItemSchema(ma.Schema):

    class Meta:
        fields = ('name', 'item_bonus', 'stats')
        ordered = True