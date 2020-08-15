from flask import Flask, render_template
from imdb import get_movies

app = Flask(__name__)

@app.route("/")
def home():
    data = get_movies()
    return render_template("home.html", data=data)

app.run()