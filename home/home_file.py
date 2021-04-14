from flask import Blueprint, render_template

hm = Blueprint("home_file", __name__, template_folder="templates")

@hm.route("/")
def home():
    return render_template("home.html")