from init import db, ma
from marshmallow import fields

class Origin(db.Model):
    __tablename__ = 'origins'

    # Columns included in the origins table
    name = db.Column(db.String(30), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    breakpoints = db.Column(db.String(35), nullable= False)

    # One-to-many relationship of the origins table
    champions = db.relationship('Champion', back_populates='origin')

class OriginSchema(ma.Schema):
    champion = fields.Nested('ChampionSchema')
    class Meta:
        fields = ('name', 'description', 'breakpoints')
