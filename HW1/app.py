from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/profile")
def profile():
    hobbies = ["NBA 시청", "축구 보기", "여행 가기"]
    return render_template("profile.html", hobbies=hobbies)

@app.route("/greet/<name>")
def greet(name):
    return render_template("greet.html", name=name)