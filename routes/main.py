from flask import Blueprint,render_template
from shared.logger import getLogger
# Create a Blueprint instance
blueprint = Blueprint('main', __name__)

@blueprint.route("/")
def index():
    return render_template("index.html")

@blueprint.route("/post/<int:id>")
def post(id):
    return f"Post ID:{id}"

@blueprint.route('/about')
def about():
    return 'The about page'

@blueprint.route("/books", methods=["GET","POST"])
def books():
    books =[{"id": 1, "name": "Book 1"},{"id": 2, "name": "Book 2"},{"id": 3, "name": "Book 3"}]
    return render_template("books.html",books=books)