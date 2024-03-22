import json
from flask import Blueprint, request, jsonify, render_template
from flask_login import login_required, current_user
from .models import Todonote, User
from . import db
from sqlalchemy import func

views = Blueprint('views', __name__)


# Home page will contain search capabilities to search through user's to do notes
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    is_home_page = True
    searchResults = []
    searchQuery = request.form.get('searchQuery')

    # Load the list of notes if there is a query
    if searchQuery:
        searchResults = Todonote.query.filter(Todonote.userid == current_user.id, func.lower(Todonote.data).like(func.lower(f'%{searchQuery}%'))).all()
        return render_template("home.html", is_home_page=is_home_page, user=current_user, searchResults=searchResults)
    return render_template("home.html", is_home_page=is_home_page, user=current_user)


# Endpoint to add to do notes to the user
@views.route('/todo', methods=['GET', 'POST'])
@login_required
def addTask():
    is_todo_page = True
    # Either load the to do list page or add a to do note or task
    if request.method =='POST':
        # Loading data from the request
        task = request.form.get('todotask')
        # Make sure that there is content in the to do note
        if len(task) > 0:
            addTask = Todonote(userid=current_user.id, data=task)
            db.session.add(addTask)
            db.session.commit()

    return render_template("todo.html", is_todo_page=is_todo_page, user=current_user)


# Used to delete to do notes from the database
@views.route('/deletetask', methods=['POST'])
def deleteTask():
    # Loading data from request
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Todonote.query.get(taskId)

    # Make sure that there is a task to delete
    if task:
        if current_user.id == task.userid:
            db.session.delete(task)
            db.session.commit()

    # Return blank because we do not need anything from it
    return jsonify({})

