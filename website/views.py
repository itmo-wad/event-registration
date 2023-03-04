from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():

    # query2= {"_id": id}
    #
    # details1 = mongo.db.events.find_one(query2)

    return render_template(f'pages/index.html')#, n=details1)


@views.route('/event-page')
def eventSpecification():
    return render_template('event-page.html')
