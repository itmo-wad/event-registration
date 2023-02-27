from flask import Flask,render_template



def page_not_found(e):
  return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'somerandkey'

    from .views import views
    from .auth import auth
    from .admin import admin

    app.register_error_handler(404, page_not_found)
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    return app