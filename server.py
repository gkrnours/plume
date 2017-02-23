#! /usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "plume"


if __name__ == "__main__":
    app.run("0.0.0.0", "5000")
