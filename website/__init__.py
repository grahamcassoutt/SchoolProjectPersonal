from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "database.db"
# Initialization of application with database
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'valueOF433'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'


    db.init_app(app)
    create_db(app)
    migrate = Migrate(app, db)

    from .views import views
    from .authentication import authentication
    from .models import User, Todonote

    # Loading in the endpoints in views and authentication to app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')


    # Need this to redirect if user they are not logged in
    login_manager = LoginManager()
    login_manager.login_view = '/login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def loadUser(id):
        return User.query.get(int(id))

    return app

# Creates database if there is not already a database created
def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('DB Created')