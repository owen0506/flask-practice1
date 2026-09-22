# app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hi/<name>")
def hi_template_render(name):
    return render_template("hi.html", name=name)

app.run(debug=True)