from flask import Flask, request, render_template

from app import App

flask_app = Flask(__name__)


@flask_app.route("/")
def index():
    return render_template("index.html")


@flask_app.route("/search")
def search():
    search_query = request.args.get("search_query")

    app = App()
    results = app.search(search_query, results=5)
    return results
