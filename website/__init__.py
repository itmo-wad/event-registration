from flask import Flask,render_template
from flask_pymongo import PyMongo
from os import *

# Mongodb client
mongo = PyMongo()
DB_NAME = "Eventhandler"

# collection for the usersprofile




def page_not_found(e):
  return render_template('404.html'), 404


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'somerandkey' #secure cookies and sessions
    app.config["MONGO_URI"] = f"mongodb://localhost:27023/{DB_NAME}"
    mongo.init_app(app)



    from .views import views    #importing files from other files
    from .auth import auth      #importing files from other files
    from .admin import admin       #importing files from other files

    app.register_error_handler(404, page_not_found)
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')



    return app