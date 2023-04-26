from init import db

class Complaint(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    complaint = db.Column(db.String(50), unique = True, nullable=False)

