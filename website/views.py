from flask import Blueprint,render_template

views = Blueprint('views', __name__)


# @app.route("/")
# def index():
#     if 'username' in session:
#         return render_template(f'pages/index.html')

#     # Render authentication form at http://localhost:5000/
#     return redirect(url_for("auth_page.sign_in"))

@views.route('/')
def home():
    return render_template(f'pages/index.html')