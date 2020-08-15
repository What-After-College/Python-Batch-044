from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>welcome to home page</h1>"

@app.route("/status")
def status():
    return "welcome to status page"

@app.route("/<name>")
def dynroute(name):
    lis = [4,5,6]
    return "my name is "+name + str(lis)

app.run(debug=True)