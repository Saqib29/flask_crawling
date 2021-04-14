from flask import Flask
from instagram.file import insta
from home.home_file import hm

app = Flask(__name__)

app.register_blueprint(hm, url_prefix="/")
app.register_blueprint(insta, url_prefix="/instagram")

# @app.route("/")
# def home():
#     return "<h1>Hello to Home</h1>"


if __name__ == "__main__":
    app.run(debug=True)