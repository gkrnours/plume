from datetime import datetime

import peewee
from playhouse.flask_utils import FlaskDB

db_wrapper = FlaskDB()


class Author(db_wrapper.Model):
    name = peewee.CharField(max_length=160)


class Content(db_wrapper.Model):
    HIDDEN = 'hd'
    DRAFT  = 'df'
    PUBLISHED = 'pb'
    STATUS_CHOICES = (
        (HIDDEN, 'Hidden'),
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published'),
    )
    PAGE = 'pg'
    ARTICLE = 'ar'
    QUOTE = 'qt'
    TYPE_CHOICES = (
        (PAGE, 'Page'),
        (ARTICLE, 'Article'),
        (DRAFT, 'Draft'),
        (QUOTE, 'Quote'),
    )

    author = peewee.ForeignKeyField(Author, related_name="publications")
    title = peewee.CharField(max_length=160)
    content = peewee.TextField()
    slug = peewee.CharField(max_length=40)
    date = peewee.DateTimeField(default=datetime.now)
    modified = peewee.DateTimeField(default=datetime.now)
    status = peewee.CharField(max_length=2, choices=STATUS_CHOICES)


if __name__ == "__main__":
    from server import app
    db_wrapper.init_app(app)

    db = db_wrapper.database
    db.connect()
    db.create_tables([Author, Content])
    db.close()
