from flask import Flask

app = Flask(__name__)

@app.route("/")
def beranda():
    return "Hallo"

@app.route("/setting")
def setting():
    return "Anda masuk ke halaman setting..."

@app.route("/profile/<username>")
def profile(username):
    return "Anda masuk ke halaman profile %s" % username

@app.route("/blog/<int:blog_id>")
def blog(blog_id):
    return "Anda masuk ke halaman blog nomor %d" % blog_id