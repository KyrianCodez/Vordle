import re
from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import current_user, login_required
import json

from App.controllers import (
    logout_route,
    start_game,
    end_game
)
from App.controllers.game import compare_word, get_current_game, handle_response

auth_views= Blueprint('auth_views', __name__, template_folder='../templates/auth')

@auth_views.route('/logout',methods=['POST'])
@login_required
def logout():
    return logout_route()
@auth_views.route('/start', methods=['GET','POST'])
@login_required
def start():
    user = current_user._get_current_object()
    return json.dumps(start_game(user.id, "Time Attack"))
@auth_views.route('/end', methods=['GET','POST'])
@login_required
def end():
    user = current_user._get_current_object()
    return json.dumps(end_game(user.id))
@auth_views.route('/check', methods=['GET','POST'])
@login_required
def check_word():
    user = current_user._get_current_object()
    data  = request.get_json()
    game = get_current_game(user.id)
    if game.get_chance() != 0:
       
        return json.dumps(handle_response( compare_word(data['word'], game), game, 60))
    # response = compare_word(data['word'], game)
    # if(handle_response(response, game, 60) == 

@auth_views.route('/query', methods=['GET','POST'])
@login_required
def query_word():
    user = current_user._get_current_object()
    game = get_current_game(user.id)
    return json.dumps(game.toDict())


    
  