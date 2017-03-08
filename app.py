from flask import Flask
from peewee import SqliteDatabase

DATABASE = "plume.db"

app = Flask(__name__)
app.config.from_object(__name__)
db = SqliteDatabase(None, threadlocals=True)
