from init import db, ma
from marshmallow import fields

class Teamboard(db.Model):
    __tablename__ = 'teamboards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text)
    
    user_username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

class TeamboardSchema(ma.Schema):
    user = fields.Nested('UserSchema')
    champions = fields.List(fields.Nested('ChampionSchema'))

    class Meta:
        fields = ('id', 'title', 'description', 'name')
        ordered = True