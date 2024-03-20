from flask import Blueprint, render_template, request, flash, redirect
from .models import User, ToDoNote
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

authentication = Blueprint('authentication', __name__)

@authentication.route('/signup', methods=['GET', 'POST'])
def signup():
    is_signup_page = True
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('This email already exist', category='error')
        if len(name) < 2:
            flash('Name must be more than 2 Characters', category='error')
        if len(email) < 5:
            flash('Email must be longer.', category='error')
        if len(password) < 2:
            flash('Password must be more than 2 Characters.', category='error')
        if len(name) >= 2 and len(email) >= 5 and len(password) >= 2 and not user:
            newUser = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            flash('Account Successfully created!', category='success')
            return redirect('/')

    data = request.form
    print(data)
    return render_template("signup.html")

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    is_login_page = True
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                return redirect('/')
            else:
                flash('Incorrect Password.', category='error')
        else:
            flash('Email not in use.', category='error')
    return render_template("login.html")

@authentication.route('/logout')
def logout():
    is_logout_page = True

    return "<p>Logout</p>"