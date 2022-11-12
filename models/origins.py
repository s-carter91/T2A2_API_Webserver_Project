from init import db, ma
from marshmallow import fields

class Origin(db.Model):
    __tablename__ = 'origins'

    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    breakpoints = db.Column(db.String(35))

    champions = db.relationship('Champion', back_populates='origin')

class OriginSchema(ma.Schema):
    champion = fields.Nested('ChampionSchema')
    class Meta:
        fields = ('name', 'description', 'breakpoints')
