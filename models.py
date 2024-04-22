""" Створення моделей. """

from mongoengine import StringField, Document, ListField, ReferenceField

class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Qoutes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule='CASCADE')
    qoute = StringField()