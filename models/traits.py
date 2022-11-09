from init import db, ma

class Trait(db.Model):
    __tablename__ = 'traits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    breakpoints = db.Column(db.String(20))

class TraitSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'description', 'breakpoints')
        ordered = True