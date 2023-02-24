from website import create_app
from website.controllers.auth import auth_page


app = create_app()
app.register_blueprint(auth_page, url_prefix='/auth')


if __name__ == '__main__':
    app.run(debug=True)