from flask import redirect, request, url_for
from pelicansqlgenerator.models import Content
from playhouse.flask_utils import get_object_or_404
from slugify import slugify

from plume.app import app
from plume.utils import templated
from plume.forms import PageForm

__all__ = ["page", "page_create", "page_edit", "page_delete"]


@app.route("/page/")
@templated()
def page():
    ctx = {}
    ctx["page_list"] = Content.select()
    return ctx

@app.route("/page/create/", methods=['POST', 'GET'])
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

@app.route("/page/<int:pk>/edit/", methods=['POST', 'GET'])
@templated()
def page_edit(pk):
    page = get_object_or_404(Content.select(), (Content.id == pk))
    form = PageForm(request.form, obj=page)

    if request.method == 'POST':
        if form.validate():
            form.populate_obj(page)
            page.save()
            return redirect(url_for("page"))
    return {"form": form}

@app.route("/page/<int:pk>/delete/", methods=['POST', 'GET'])
@templated()
def page_delete(pk):
    page = get_object_or_404(Content.select(), (Content.id == pk))

    if request.method == "POST":
        page.delete_instance()
        return redirect(url_for("page"))
    return {"page": page}
