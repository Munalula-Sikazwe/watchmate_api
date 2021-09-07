from django.db import models

# Create your models here.
from django.db.models import CASCADE


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    story_line = models.TextField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform,on_delete=CASCADE,related_name='watchlist')

    def __str__(self):
        return self.title


