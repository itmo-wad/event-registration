from flask import Blueprint, redirect, render_template, request, session, url_for

admin = Blueprint("admin", __name__, template_folder='templates')


@admin.route('/admin', methods=["GET", "POST"])
def index():
    return redirect(f'/admin/events')

@admin.route('/admin/events', methods=["GET", "POST"])
def events():
    return render_template(f'pages/admin/events.html')


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
