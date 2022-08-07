from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
login_manager = LoginManager()
DB_Name = "rentNaTeknoy.db"

def create_website():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "RentNaTeknoyAdmin123"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    db.init_app(app)

    from App.Dashboard.route import Dashboard
    from App.UserProfile.route import UserProfile
    from App.Forms.route import Forms
    from App.Home.route import Home

    app.register_blueprint(Dashboard, url_prefix="/")
    app.register_blueprint(UserProfile, url_prefix="/")
    app.register_blueprint(Forms, url_prefix="/")
    app.register_blueprint(Home, url_prefix="/")

    from App.models import User, Reviews

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = "Forms.SigninPage"
    login_manager.init_app(app)
    


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists('App/' + DB_Name):
        db.create_all(app=app)
        print('Created Database!')


    
