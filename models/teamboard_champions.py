from init import db, ma

# Or is it .Model??
class Associatio(db.Base):
    __tablename__ = "teamboards_champions"
    teamboard_id = db.Column(db.ForeignKey("teamboards.id"), primary_key=True)
    right_id = db.Column(db.ForeignKey("champions.id"), primary_key=True)
    extra_data = db.Column(db.String(50))
    child = db.relationship("Child")