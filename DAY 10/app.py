from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/second")
def second():
    name1="Neeraj Sharma"
    n=6
    return render_template("second.html", name2 = name1,n=n)

@app.route("/third")
def third():
    city = {
        "city_name" : "Delhi",
        "Temp" : "96F",
        "climate" : "strom"
    }
    return city

app.run(debug=True)