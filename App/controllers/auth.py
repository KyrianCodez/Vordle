from flask import flash
from flask_login import login_user, logout_user, LoginManager, current_user
from flask_jwt import JWT
from App.models import User
import json

login_manager = LoginManager()
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return User.query.get(payload['identity'])

def login_route(user):
    try:
        user = User.query.filter_by(username = user['username']).first()
        if login_user(user):
            user.set_auth(True)
            return user
    except:
        return False

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
    

def logout_route():
    user = current_user._get_current_object()
    user.set_auth(False)
    logout_user()
    return True
def setup_jsf(app):
    return jsf.use(app) 
def setup_login(app):
    return login_manager.init_app(app)
def setup_jwt(app):
    return JWT(app, authenticate, identity)