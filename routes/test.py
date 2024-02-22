from flask import Blueprint,render_template, abort
from markupsafe import escape
import json

# Create a Blueprint instance
blueprint = Blueprint('test', __name__)



@blueprint.route("/hello")
def hello():
    return render_template("index.html")

# @blueprint.route("/<name>")
# def name(name):
#     return f"Hello, {escape(name)}!"

@blueprint.route('/login')
def login():
    return abort(404)