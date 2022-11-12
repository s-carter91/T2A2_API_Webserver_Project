from init import db, ma

# class Item(db.Model):
#     __tablename__ = 'items'

#     # id = db.Column(db.Integer, )
#     name = db.Column(db.String(30), primary_key=True)
#     item_bonus = db.Column(db.Text, nullable=False)
#     stats = db.Column(db.String(50))

# class ItemSchema(ma.Schema):

#     class Meta:
#         fields = ('name', 'item_bonus', 'stats')
#         ordered = True