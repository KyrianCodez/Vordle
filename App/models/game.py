from email.policy import default
from App.database import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id',db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer)
    mode = db.Column(db.String(50))
    chance = db.Column(db.Integer,nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    word_id = db.Column('word_id',db.Integer, db.ForeignKey('word.id'))
    word = db.relationship('Word')

    def __init__(self,user_id, mode, word_id):
        self.user_id = user_id
        self.score = 0
        self.chance = 5
        self.active = True
        self.word_id = word_id
        self.mode = mode

    def get_active(self):
        return self.active

    def set_active(self,active):
        self.active = active
        db.session.add(self)
        db.session.commit()
    def get_chances(self):
        return self.chance
    def update_chance(self):
        self.chance = self.chance - 1
        db.session.add(self)
        db.session.commit()
    def toDict(self):
        return {
            "score": self.score,
            "chance": self.chance,
            "active": self.active,
            "word": self.word.toDict()
        }
        
    