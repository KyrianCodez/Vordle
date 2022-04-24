from webbrowser import get
from flask import Blueprint, flash, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import current_user, login_required
import json

from App.controllers import (
    logout_route,
    start_game,
    end_game,
    check_response,
    start_new_round,
    compare_word, 
    get_current_game, 
    handle_incorrect,
    order_by_score

)
from App.controllers.game import check_response
from App.views.user import login

auth_views= Blueprint('auth_views', __name__, template_folder='../templates')

@auth_views.route('/logout',methods=['GET'])
@login_required
def logout():
    if logout_route():
        flash("Logout Success")
        return render_template("/guest/index.html")
@auth_views.route('/start', methods=['GET','POST'])
@login_required
def start():
    user = current_user._get_current_object()
    game = start_game(user.id, "Time Attack")
    return render_template('/auth/game.html', game = game.toDict())
@auth_views.route('/end', methods=['GET','POST'])
@login_required
def end():
    user = current_user._get_current_object()
    end_game(user)
    return render_template('/auth/menu.html')
@auth_views.route('/check', methods=['POST'])
@login_required
def check_word():
    user = current_user._get_current_object()
    data  = request.get_json()
    game = get_current_game(user.id)
    response = compare_word(data['word'], game)
    eval = check_response(response)
    responseDict = {
        "response" : response,
        "isCorrect" : eval,
        "chances" : game.get_chances()
    }
    if eval == True:
        return json.dumps(responseDict)
    if handle_incorrect(game):
        return json.dumps(responseDict)
@auth_views.route('/new_round', methods=['GET'])
@login_required
def new_round():
    user = current_user._get_current_object()
    if start_new_round(get_current_game(user.id)):
        new_round = get_current_game(user.id)
        return json.dumps(new_round.toDict()) 
@auth_views.route('/query', methods=['GET','POST'])
@login_required
def query_word():
    user = current_user._get_current_object()
    game = get_current_game(user.id)
    return json.dumps(game.toDict())
@auth_views.route('/leaderboard', methods=['GET'])
@login_required
def get_leaderboard():
    return render_template('/auth/leaderboard.html',rankings = order_by_score())


    
@auth_views.route('/profile')
@login_required
def edit_profile():
    user = current_user._get_current_object()
    return render_template('/auth/details.html', user=user)

