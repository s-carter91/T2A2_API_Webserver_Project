from init import db, ma
from marshmallow import fields

class Origin(db.Model):
    __tablename__ = 'origins'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    breakpoints = db.Column(db.String(20), nullable=False)

    champions = db.relationship('Champion', backref='origins')

class OriginSchema(ma.Schema):
    champion = fields.Nested('ChampionSchema')
    class Meta:
        fields = ('id', 'name', 'description', 'breakpoints')
