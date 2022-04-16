from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import login_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    login_route
)


guest_views = Blueprint('user_views', __name__, template_folder='../templates/guest')


@guest_views.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if create_user(data['username'], data['password']):
        return login_route(data)
    return "User already exists"

@guest_views.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return login_route(data)
  
  
    
@guest_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@guest_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@guest_views.route('/api/lol')
def lol():
    return 'lol'

@guest_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')