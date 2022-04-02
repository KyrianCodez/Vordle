from email.policy import default
from App.database import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer)
    mode = db.Column(db.String(50), default="Time Attack")
    chance = db.Column(db.Integer, default="5", nullable = False)
    active = db.Column(db.Boolean, default=True, nullable = False)
    auth = db.Column(db.Boolean, default=False, nullable = False)
    anon = db.Column(db.Boolean, default=False, nullable = False) 