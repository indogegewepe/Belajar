from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/profile/<username>")
def profile(username):
    return render_template("profile.html", username1=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        return "Email kamu adalah " + request.form['email']

    return render_template("login.html")