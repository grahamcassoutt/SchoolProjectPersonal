import json
from flask import Blueprint, request, jsonify, render_template, flash
from flask_login import login_required, current_user
from .models import Todonote, User
from . import db
from sqlalchemy import func

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    is_home_page = True
    searchResults = []
    searchQuery = request.form.get('searchQuery')

    if searchQuery:
        searchResults = Todonote.query.filter(Todonote.userid == current_user.id, func.lower(Todonote.data).like(func.lower(f'%{searchQuery}%'))).all()
        return render_template("home.html", is_home_page=is_home_page, user=current_user, searchResults=searchResults)
    return render_template("home.html", is_home_page=is_home_page, user=current_user)

@views.route('/todo', methods=['GET', 'POST'])
@login_required
def addTask():
    is_todo_page = True
    if request.method =='POST':
        task = request.form.get('todotask')
        if len(task) > 0:
            addTask = Todonote(userid=current_user.id, data=task)
            db.session.add(addTask)
            db.session.commit()

    return render_template("todo.html", is_todo_page=is_todo_page, user=current_user)

@views.route('/deletetask', methods=['POST'])
def deleteTask():
    task = json.loads(request.data)
    taskId = task['taskId']
    task = Todonote.query.get(taskId)
    if task:
        if current_user.id == task.userid:
            db.session.delete(task)
            db.session.commit()


    return jsonify({})

