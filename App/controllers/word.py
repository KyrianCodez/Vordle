from sqlite3 import IntegrityError
from App.models import Word
from App.database import  db
from random import randint


def get_all_words_as_list():
    words = Word.query.all()
    if not words:
        return []
    return words
def wordify(word):
    return Word(word,None,None)

def word_exists(word):
    database = get_all_words_as_list
    w = wordify(word)
    for word in database:
        if(word.__eq__(word)):
            return True
    return False
def add_word(word,partsOfSpeech,meaning):
    new_word = Word(word,partsOfSpeech,meaning)
    try:
        db.session.add(new_word)
        db.session.commit()
    except:
        db.session.rollback
        print('Word failed to add')
    print('Word added')

def get_random_word():
    words = get_all_words_as_list()
    index = randint(0,len(words))
    return words[index]
