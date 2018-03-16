from django.db import models
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

#TODO: need photos

    def __str__(self):
        return self.title


