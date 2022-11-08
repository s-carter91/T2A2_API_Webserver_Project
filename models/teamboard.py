from init import db

class Teamboard(db.Model):
    __tablename__ = 'teamboards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text)
    