from flask_app import db

class Journal(db.Model):
    __tablename__ = "journals"

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    entry1 = db.Column(db.Text)
    entry2 = db.Column(db.Text)
    entry3 = db.Column(db.Text)
    image = db.Column(db.String(200))
    mood = db.Column(db.Integer)