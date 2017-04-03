#! /usr/bin/env python
from pelicansqlgenerator import models
from playhouse import db_url

from app import app
import views

def main():
    db = db_url.connect(app.config["DATABASE"])
    models.database.initialize(db)
    app.run("0.0.0.0", 5000, debug=True)

if __name__ == "__main__":
    main()
