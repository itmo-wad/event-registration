from flask import Blueprint, render_template, session, redirect, url_for, request, flash, make_response
import re
from werkzeug.security import generate_password_hash, check_password_hash
# from .model import user

from website import mongo


auth = Blueprint('auth', __name__)


@auth.route('auth/sign-in', methods=["GET", "POST"])
def sign_in():
    user_in_session = 'email' in session
    if user_in_session:
        # flash('Logged back in successfully', 'other')
        return redirect(url_for(f'/pages/index.html'))

    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        if not email or len(email) == 0:
            flash('You have not provided an email', 'danger')
        elif not password or len(password) == 0 :
            flash('You have not provided a password', 'danger')
        else:
            existing_email = mongo.db.users.find_one({'email': email})
            if not existing_email:
                flash('Wrong login or password', 'danger')
            if check_password_hash(existing_email['password'], password) == False:
                flash('Wrong login or password', 'danger')
            else:
                flash('Logged in successfully.', 'success')
                resp = make_response(redirect(url_for('views.home')))
                session['email'] = email
                return resp
    return render_template(f'pages/auth/sign-in.html')


@auth.route('auth/register', methods=["GET", "POST"])
def sign_up():
    user_in_session = 'email' in session
    if user_in_session:
        # flash('Logged back in successfully', 'success')
        return redirect(url_for(f'/pages/index.html'))

    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        con_password = request.form.get('confirm_password')
        fullname = request.form.get('fname')

        # Define a regular expression pattern for valid email addresses
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #123@,..tttt.com

        # Check if email address matches the pattern and conditions
        if not re.match(pattern, email):
            flash('Incorrect Email', category='error')
        elif len(password)<8 or password != con_password:
            flash('Password must be at least 8 characters or passwords don\'t match', category="error")
        elif len(fullname) < 2:
            flash('Fullname is too short. Enter Your First Name and Last Name', category="error")
        else:
            #add user to the database

            existing_email = mongo.db.users.find_one({'email': email})

            if existing_email:
                flash('This email is already taken, please choose another one', 'danger')
                return redirect(f'pages/auth/register.html')
            else:
                encrypted_password1 = generate_password_hash(password)
                encrypted_password2 = generate_password_hash(con_password)

                mongo.db.users.insert_one(
                {'email': email, 'password': encrypted_password1,
                 'con_password': encrypted_password2, 'Full Name': fullname})
            flash('Account Created Succesfully', category="success")

            session['email'] = email
            return redirect(f'/pages/index.html')

    return render_template(f'pages/auth/register.html')


@auth.route('/sign-out')
def sign_out():
    session.pop('email', None)
    return redirect(url_for('index'))
