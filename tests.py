import os
import unittest
import tempfile

from app import app, db
import models
import views


class PlumeTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.db_fd, self.db_fn = tempfile.mkstemp()
        models.init_db(self.db_fn)

    def tearDown(self):
        db.close()
        os.close(self.db_fd)
        os.unlink(self.db_fn)

    def test_urls(self):
        rv = self.app.get("/page")
        assert 301 == rv.status_code
        assert "http://localhost/page/" == rv.location
        rv = self.app.get("/page/")
        assert 200 == rv.status_code

    def test_no_data(self):
        rv = self.app.get("/page/")
        assert b"no pages" in rv.data

if __name__ == '__main__':
    unittest.main()

