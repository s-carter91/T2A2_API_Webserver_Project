from init import db, ma

class User(db.Model):
    __tablename__ = 'users'

    # Columns included in the users table
    username = db.Column(db.String(25), primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # One-to-many relationship of the users table
    teamboards = db.relationship('Teamboard', back_populates='user',  cascade='all, delete-orphan')
    
class UserSchema(ma.Schema):

    class Meta:
        fields = ('username', 'email', 'password', 'is_admin')
        ordered = True