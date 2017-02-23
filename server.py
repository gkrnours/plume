#! /usr/bin/env python
from flask import Flask

from utils import templated

app = Flask(__name__)

@app.route("/")
@templated()
def home():
    pass


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
