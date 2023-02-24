from flask import Blueprint, redirect, render_template, request, session, url_for

auth_page = Blueprint("auth_page", __name__, template_folder='templates/auth')

@auth_page.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    return render_template(f'pages/auth/sign-in.html')

@auth_page.route('/register', methods=["GET", "POST"])
def sign_up():
    return render_template(f'pages/auth/register.html')

@auth_page.route('/sign-out')
def sign_out():
    session.pop('username', None)
    return redirect(url_for('index'))