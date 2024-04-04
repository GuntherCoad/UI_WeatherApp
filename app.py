from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/temp")
def temp():
    return render_template("tempPage.html")
