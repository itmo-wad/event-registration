from flask import Blueprint, render_template

from website import mongo

views = Blueprint('views', __name__)


# @app.route("/")
# def index():
#     if 'username' in session:
#         return render_template(f'pages/index.html')

#     # Render authentication form at http://localhost:5000/
#     return redirect(url_for("auth_page.sign_in"))

@views.route('/', methods=['GET', 'POST'])
def home():

    # query2= {"_id": id}
    #
    # details1 = mongo.db.events.find_one(query2)

    return render_template(f'pages/index.html')#, n=details1)


@views.route('/event-page')
def eventSpecification():
    return render_template('event-page.html')
