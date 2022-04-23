from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.views import guest_views



@guest_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('/guest/index.html')
