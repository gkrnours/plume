from os import path
from flask import Flask

DATABASE = "sqlite:///%s" % path.join(path.dirname(__file__), "plume.db")

app = Flask(__name__)
app.config.from_object(__name__)
