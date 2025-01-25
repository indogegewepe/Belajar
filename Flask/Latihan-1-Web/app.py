from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello BosQu!!'

# $env:FLASK_APP="apppy"                flask run


# $env:FLASK_APP = "app.py"
# $env:FLASK_DEBUG = "1"
# python -m flask run