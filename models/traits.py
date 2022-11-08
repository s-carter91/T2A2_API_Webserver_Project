from init import db

class Trait(db.Model):
    __tablename__ = 'traits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
