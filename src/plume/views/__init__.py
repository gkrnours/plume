import os

from flask import send_from_directory

from plume.app import app
from plume.utils import templated

from .page import *


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                'favicon.ico', mimetype='image/png')

@app.route("/")
@templated()
def home():
    pass
