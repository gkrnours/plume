import os
import unittest
import tempfile

from flask import url_for

from app import app, db


class PlumeTest(unittest.TestCase):
    def setUp(self):
        import models
        import views # without it, app have no route
        app.config["TESTING"] = True
        app.config["SERVER_NAME"] = "localhost"
        self.client = app.test_client()
        self.db_fd, self.db_fn = tempfile.mkstemp()
        models.init_db(self.db_fn)

    def tearDown(self):
        db.close()
        os.close(self.db_fd)
        os.unlink(self.db_fn)

    def test_urls(self):
        # url_for require a context
        with app.app_context():
            rv = self.client.get("/page")
            assert 301 == rv.status_code
            assert url_for("page") == rv.location
            for url in ["page", "page_create"]:
                rv = self.client.get(url_for(url))
                assert 200 == rv.status_code, "Error for %s" % url
            for url in ["page_edit", "page_delete"]:
                rv = self.client.get(url, data={"pk":1})
                assert 200 == rv.status_code, "Error for %s" % url

    def test_no_data(self):
        rv = self.client.get("/page/")
        assert b"no pages" in rv.data

    def test_save(self):
        from models import Content
        with app.app_context():
            url = url_for("page_create")
        rv = self.client.post(url, data=dict(
            title="page test", content="# Page Title", author="1", status="pb"
        ), follow_redirects=True)
        assert 200 == rv.status_code
        assert 1 == Content.select().count()

if __name__ == '__main__':
    unittest.main()

