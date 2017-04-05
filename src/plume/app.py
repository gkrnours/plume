from os import path
import random
import string
from flask import Flask

DATABASE = "sqlite:///%s" % path.join(path.dirname(__file__), "plume.db")
SECRET_KEY = "".join(random.choice(string.lowercase) for i in range(10))

app = Flask(__name__)
app.config.from_object(__name__)
