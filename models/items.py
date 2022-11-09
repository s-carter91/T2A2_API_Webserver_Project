from init import db, ma

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    item_bonus = db.Column(db.Text, nullable=False)
    stats = db.Column(db.String(50))

class ItemSchema(ma.Schema):

    class Meta:
        fields = ('id', 'name', 'description')
        ordered = True