from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    is_home_page = True
    return '<h1>Hello, World!</h1>'