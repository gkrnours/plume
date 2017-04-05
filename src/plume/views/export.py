from __future__ import unicode_literals

import os
import tempfile

from flask import redirect, request, session, url_for
from pelican import Pelican
from pelican.settings import read_settings

from plume.app import app
from plume.utils import Capturing, templated

__all__ = ["export", "export_random"]


@app.route("/export/")
@templated()
def export():
    pass

@app.route("/export/random/", methods=["GET", "POST"])
@templated()
def export_random():
    if request.method == "POST":
        # Build settings
        p_dir = session["dir"] = tempfile.mkdtemp(prefix="plume.")
        p_empty = tempfile.mkdtemp(prefix="pelican.")
        p_settings = read_settings(path=p_empty, override={
            "OUTPUT_PATH": p_dir,
            "PLUGINS": ["pelicansqlgenerator"],
            "SQL_DATABASE": app.config["DATABASE"],
        })
        # Build the site
        with Capturing() as output:
            Pelican(settings=p_settings).run()
        session["output"] = output
    return {
        "dir": session["dir"],
        "output": "\n".join(session["output"]),
        "result": os.listdir(session["dir"]),
    }
