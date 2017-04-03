import os
import unittest
import tempfile

from flask import url_for
from playhouse import db_url

from plume.app import app


class PlumeTest(unittest.TestCase):
    def setUp(self):
        from pelicansqlgenerator import models
        from plume import views
        # without importing views, app have no route
        app.config["TESTING"] = True
        app.config["SERVER_NAME"] = "localhost"
        self.client = app.test_client()
        self.db_fd, self.db_fn = tempfile.mkstemp()
        self.db = db_url.connect("sqlite:///%s" % self.db_fn)
        models.database.initialize(self.db)
        models.init_db(self.db)

    def tearDown(self):
        self.db.close()
        os.close(self.db_fd)
        os.unlink(self.db_fn)

    def test_urls(self):
        # url_for require a context
        with app.app_context():
            # url not ending with a slash redirect
            rv = self.client.get("/page")
            assert 301 == rv.status_code
            assert url_for("page") == rv.location
            # These page don't need data
            for url in ["page", "page_create"]:
                rv = self.client.get(url_for(url))
                assert 200 == rv.status_code, "Error for %s" % url
            # These page produce 404 without data
            for url in ["page_edit", "page_delete"]:
                rv = self.client.get(url_for(url, pk="1"))
                assert 404 == rv.status_code, "Error for %s" % url
            # Inserting data in db should fix the issue
            from pelicansqlgenerator import models
            models.Content.create(id=1, title="foo", content="bar", author=1,
                    slug="foo", status="hd")
            for url in ["page_edit", "page_delete"]:
                rv = self.client.get(url_for(url, pk="1"))
                assert 200 == rv.status_code, "Error for %s" % url

    def test_no_data(self):
        rv = self.client.get("/page/")
        assert b"no pages" in rv.data

    def test_save(self):
        from pelicansqlgenerator import models
        with app.app_context():
            url = url_for("page_create")
        rv = self.client.post(url, data=dict(
            title="page test", content="# Page Title", author="0", status="pb"
        ), follow_redirects=True)
        assert 200 == rv.status_code
        assert 1 == models.Content.select().count()

if __name__ == '__main__':
    unittest.main()

