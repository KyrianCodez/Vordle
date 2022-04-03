from App.database import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(120))
    partOfSpeech =  db.Column(db.String(120))
    meaning = db.Column(db.String(500))

    def word_listify(self):
        return list(self.word)

    def __init__(self, word, partOfSpeech, meaning):
        self.word = word
        self.partOfSpeech = partOfSpeech
        self.meaning = meaning
    def get_word(self):
        return self.word
    def __eq__(self, word):
        if isinstance(word, Word):
            return self.get_word() == word.get_word()
        return False 
    

    def toDict(self):   
        return{
            'id' : self.id,
            'word' : self.word,
            'partOfSpeech':self.partOfSpeech,
            'meaning':self.meaning
        }
