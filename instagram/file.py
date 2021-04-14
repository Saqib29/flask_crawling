from flask import Blueprint

insta = Blueprint("file", __name__)

@insta.route("/")
def home():
    return "<h1>Hello from instagram</h1>"