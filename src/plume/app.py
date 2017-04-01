from os import path
from flask import Flask
from peewee import SqliteDatabase

DATABASE = path.join(path.dirname(__file__), "plume.db")

app = Flask(__name__)
app.config.from_object(__name__)
db = SqliteDatabase(None, threadlocals=False)
