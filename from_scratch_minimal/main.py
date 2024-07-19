from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route("/")
def hello():
    return send_from_directory("", "index.html")
