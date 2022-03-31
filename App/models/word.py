from App.database import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(120))
    partOfSpeech =  db.Column(db.String(120))
    meaning = db.Column(db.String(500))

    def __init__(self, word, partOfSpeech, meaning):
        self.word = word
        self.partOfSpeech = partOfSpeech
        self.meaning = meaning
        
    def toDict(self):
        return{
            'id' : self.id,
            'word' : self.word,
            'partOfSpeech':self.partOfSpeech,
            'meaning':self.meaning
        }
