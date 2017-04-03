from wtfpeewee.orm import model_form

from pelicansqlgenerator import models

PageForm = model_form(models.Content, 
    only=("author", "title", "status", "content"))
