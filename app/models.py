from flask_app import db

class Journal(db.Model):
    __tablename__ = "journals"

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    prompt = db.Column(db.String(200))
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))
    about = db.Column(db.String(200))
    entry1 = db.Column(db.String(200))
    entry2 = db.Column(db.String(200))
    entry3 = db.Column(db.String(200))
    question1 = db.Column(db.String(200))
    question2 = db.Column(db.String(200))
    question3 = db.Column(db.String(200))
    mood = db.Column(db.Integer)

class Mood(db.Model):
    __tablename__ = 'moods'

    id = db.Column(db.Integer, primary_key=True)
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    mood = db.Column(db.Integer)
