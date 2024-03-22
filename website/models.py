from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import uuid


# A Todonote can only belong to one User
class Todonote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data =db.Column(db.String(5000))
    # Sets date to current time
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # A Todonote can only belong to one User
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Need to init when creating a new todonote
    def __init__(self, userid, data):
        self.userid = userid
        self.data = data



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    # A User can have multiple Todonotes
    todonotes = db.relationship('Todonote', backref='user', lazy=True)


    # Need to init when creating a new user
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password