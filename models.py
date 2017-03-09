from datetime import datetime

import peewee

from app import app, db


class Author(peewee.Model):
    class Meta:
        database = db
    name = peewee.CharField(max_length=160)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Content(peewee.Model):
    class Meta:
        database = db
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
    slug = peewee.CharField(max_length=40)
    date = peewee.DateTimeField(default=datetime.now)
    modified = peewee.DateTimeField(default=datetime.now)
    status = peewee.CharField(max_length=2, choices=STATUS_CHOICES)
    content = peewee.TextField()

def init_db(database=None):
    if not database:
        database = app.config["DATABASE"]
    db.init(database)
    db.connect()
    db.create_tables([Author, Content])
    Author.create(id=1, name="author")
    db.close()

if __name__ == "__main__":
    init_db()
