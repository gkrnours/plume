#! /usr/bin/env python
from app import app, db
import views

if __name__ == "__main__":
    db.init(app.config["DATABASE"])
    app.run("0.0.0.0", 5000, debug=True)
