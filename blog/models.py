from __future__ import unicode_literals

from django.db import models
from time import time
# from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.
#
# def getUploadedFileName(instance, fileName):
#     return 'uploadedFiles/%s_%s/' %(str(time()).replace('.','.'), fileName)


class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UploadFile(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(null=True, blank=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.title
