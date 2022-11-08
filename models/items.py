from init import db, ma

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)

class CommentSchema(ma.schema):
    pass

    class Meta:
        fields = ('id', 'name', 'description')
        ordered = True