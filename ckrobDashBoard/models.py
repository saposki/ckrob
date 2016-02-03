from django.db import models
# Create your models here.

class Post(models.Model):
    timeCreated = models.dateTimeField(auto_now_add=True)
    title  = models.CharField(max_length=100)
    content = models.TextField()
