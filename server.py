#! /usr/bin/env python
import os

from flask import Flask
from flask import redirect, request, send_from_directory, url_for
from playhouse.flask_utils import get_object_or_404
from slugify import slugify

from utils import templated
from models import db_wrapper, Author, Content
from forms import PageForm

DATABASE = 'sqlite:///plume.db'

app = Flask(__name__)
app.config.from_object(__name__)
db_wrapper.init_app(app)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/png')

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
    form = PageForm(request.form)
    if request.method == 'POST':
        if form.validate():
            page = Content()
            form.populate_obj(page)
            page.slug = slugify(page.title)
            page.save()
            return redirect(url_for("page"))
    return {"form": form}

@app.route("/page/<int:page>/edit", methods=['POST', 'GET'])
@templated()
def page_edit(page):
    page = get_object_or_404(Content.select(), (Content.id == page))
    form = PageForm(request.form, obj=page)

    if request.method == 'POST':
        if form.validate():
            form.populate_obj(page)
            page.save()
            return redirect(url_for("page"))
    return {"form": form}



if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
