from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.


class Article(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    editor = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)

    mobile = models.CharField(max_length=20)

    joinedAt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
