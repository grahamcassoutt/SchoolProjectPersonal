from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    is_home_page = True
    return render_template('home.html', is_home_page=is_home_page)