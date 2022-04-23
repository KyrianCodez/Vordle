from flask_login import current_user
from App.controllers.user import update_highscore
from App.database import db
from App.models import Game
from App.controllers.word import *

def get_all_games():
    return Game.query.all()

def get_all_games_json():
    games = get_all_games()
    if not games:
        return []
    games = [game.toDict() for game in games]
    return games   
def get_current_game(user_id):
    game = Game.query.filter_by(user_id = user_id, active = True).first()
    return game
def get_current_game_status(game):
    return game.get_active()

def get_current_game_chances(game):
    return game.get_chance()

def update_current_game_chance(game):
    game.update_chance()
    
def update_current_game_status(game): 
    game.set_active(False)
def load_list(game):
    word_list = game.word.word_listify()
    return word_list 

    
def compare_word(word, game):
    user_word = wordify(word)
    if (word_exists(user_word)):
        response = {
            1: '',
            2: '',
            3: '',
            4: '',
            5: '',
        }
        game_list = load_list(game)
        user_word_as_list = user_word.word_listify()
        index = 0
        for ch in user_word_as_list:
            try:
                if game_list.index(ch) == user_word_as_list.index(ch):
                    response.update({index+1:'correct'})
                else:
                    response.update({index+1:'present'})
            except ValueError:
                    response.update({index+1:'absent'})
            index +=1
        return response
def check_response(response):
    if 'present' in response.values() or 'absent' in response.values():
        return False
    return True
def update_game_chance(game):
    game.update_chance()
def update_game(game):
    db.session.add(game)
    db.session.commit()
def start_new_round(game):
    try:
        word = get_random_word()
        game.reset_chance()
        game.set_word(word.id)
        game.add_to_score()
        update_game(game)
        return True
    except:
        return False
def handle_incorrect(game):
    try:
        print("Incorrect")
        game.update_chance()
        update_game(game)
        return True
    except:
        return False
       

def end_game(response):
    game = get_current_game
    if(game.get_chance() == 0):
        game.set_active(False)
        return  {
                "status": game.get_active(),
                "code" : 1
            }
    if(check_response(response)):
        game.set_active(False)
        return {
                "status": game.get_active(),
                "code" : 2
        }
def create_game(user_id, mode, word_id):
    try:
        new_game = Game(user_id = user_id, mode = mode, word_id = word_id)
        db.session.add(new_game)
        db.session.commit()
    except:
        db.session.rollback()
        return "A server side error occured", 404
    return get_current_game(user_id)
def check_active_game(user_id):
    try:
        game = get_current_game(user_id)
        if(get_current_game_status(game) == True):
                return True
    except:
        return False
def start_game(user_id, mode):
    try:
        game_in_progress = get_current_game(user_id)
        if(get_current_game_status(game_in_progress) == True):
            return game_in_progress 
    except:
        word = get_random_word()
        game = create_game(user_id, mode, word.id)
        return game
def end_game(user):
    try:
        game = get_current_game(user.id)
        game.set_active(False)
        update_highscore(user, game.score)
        db.session.add(game)
        db.session.commit()
        return True
    except:
        return "A server side error occured", 404
    

