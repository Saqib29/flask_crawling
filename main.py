from flask import Flask, flash, session
from instagram.file import insta
from home.home_file import hm
from googlesearch.script import goog

app = Flask(__name__)
app.secret_key = "secrete_key"

app.register_blueprint(hm, url_prefix="/")
app.register_blueprint(goog, url_prefix="/google")
app.register_blueprint(insta, url_prefix="/instagram")

# @app.route("/")
# def home():
#     return "<h1>Hello to Home</h1>"


if __name__ == "__main__":
    app.run(debug=True)