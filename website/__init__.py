from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'valueOF433'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)
    create_db(app)
    migrate = Migrate(app, db)

    from .views import views
    from .authentication import authentication
    from .models import User, ToDoNote

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(authentication, url_prefix='/')

    return app

def create_db(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('DB Created')