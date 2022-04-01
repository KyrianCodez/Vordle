from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import current_user, login_required
import json

from App.controllers import (
    logout_route
    
)
auth_views= Blueprint('auth_views', __name__, template_folder='../templates/auth')

@auth_views.route('/logout',methods=['POST'])
@login_required
def logout():
    return logout_route()
    
    
  