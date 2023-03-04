from flask import Blueprint, redirect, render_template, request, session, url_for

from website import mongo

admin = Blueprint("admin", __name__, template_folder='templates')


@admin.route('/admin', methods=["GET", "POST"])
def index():
    return redirect(f'/admin/events')

@admin.route('/admin/events', methods=["GET", "POST"])
def events():
    all_events = mongo.db.events.find({})
    return render_template(f'pages/admin/events.html', all_events = all_events)


@admin.route('/admin/event/create', methods=["GET", "POST"])
def create_event():
    return render_template(f'pages/admin/create_event.html')

@admin.route('/admin/event/edit', methods=["GET", "POST"])
def edit_event():
    return render_template(f'pages/admin/edit_event.html')


@admin.route('/admin/user/create', methods=["GET", "POST"])
def create_user():
    return render_template(f'pages/admin/create_user.html')


@admin.route('/admin/user/edit', methods=["GET", "POST"])
def edit_user():
    return render_template(f'pages/admin/edit_user.html')


@admin.route('/admin/users', methods=["GET", "POST"])
def users():
    return render_template(f'pages/admin/users.html')



@admin.route('/admin/club/create', methods=["GET", "POST"])
def create_club():
    return render_template(f'pages/admin/create_club.html')


@admin.route('/admin/club/edit', methods=["GET", "POST"])
def edit_club():
    return render_template(f'pages/admin/edit_club.html')


@admin.route('/admin/clubs', methods=["GET", "POST"])
def clubs():
    return render_template(f'pages/admin/clubs.html')