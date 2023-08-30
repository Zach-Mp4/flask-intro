from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "welcome"

@app.route("/welcome/home")
def home():
    return "welcome home"

@app.route("/welcome/back")
def back():
    return "welcome back"

