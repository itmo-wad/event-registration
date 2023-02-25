from flask import Blueprint,render_template,session,redirect,url_for

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    return render_template(f'pages/auth/sign-in.html')

@auth.route('/register', methods=["GET", "POST"])
def sign_up():
    return render_template(f'pages/auth/register.html')

@auth.route('/sign-out')
def sign_out():
    session.pop('username', None)
    return redirect(url_for('index'))