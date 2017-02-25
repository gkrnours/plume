#! /usr/bin/env python
from flask import Flask
from flask import redirect, request, url_for
from slugify import slugify

from utils import templated
from models import db_wrapper, Author, Content

DATABASE = 'sqlite:///plume.db'

app = Flask(__name__)
app.config.from_object(__name__)
db_wrapper.init_app(app)

@app.route("/")
@templated()
def home():
    pass

@app.route("/page")
@templated()
def page():
    ctx = {}
    ctx["page_list"] = Content.select()
    return ctx

@app.route("/page/create", methods=['POST', 'GET'])
@templated()
def page_create():
    if request.method == 'POST':
        page = Content()
        page.author = Author.get_or_create(name="author")[0]
        page.title = request.form['title']
        page.content = request.form['content']
        page.slug = slugify(request.form['title'])
        page.status = Content.DRAFT
        page.save()
        return redirect(url_for("page"))



if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
