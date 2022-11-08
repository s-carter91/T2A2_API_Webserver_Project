from init import db, ma

class Champion(db.Model):
    __tablename__ = 'champions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)

    teamboard = db.relationship('User', back_populates='Champions')

class CommentSchema(ma.schema):
    pass

    class Meta:
        fields = ('id', 'name', 'description')
        ordered = True