from init import db, ma
from marshmallow import fields

class Champion(db.Model):
    __tablename__ = 'champions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    ability = db.Column(db.Text, nullable=False)
    suggested_items = db.Column(db.Text)

    # origin_id = db.Column(db.Integer, db.ForeignKey('origin.id'), nullable=False)

class ChampionSchema(ma.Schema):
    origin = fields.Nested('OriginSchema')

    class Meta:
        fields = ('id', 'name', 'cost', 'ability', 'suggested_items')
        order_by = 'cost'
        ordered = True