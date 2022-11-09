from init import db, ma

class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(25), primary_key=True)
    # name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):

    class Meta:
        fields = ('username', 'email', 'password', 'is_admin')