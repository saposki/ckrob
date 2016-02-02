from django.db import models
from mongoengine import *

# Create your models here.

class Artifact(EmbeddedDcoument):
    description = String(max_length=200)
    rating = IntField(default=0)

class Container(Document):
    question = StringField(max_length=200)
    publicationDate = DateTimeField(help_text='data published')
    pin = ListField(EmbeddedDcoumentField(Artifact))

    meta = {
        'indexes': [
            'question',
            ('publicationDate', '+question')
        ]
    }
