from django.db import models

# Create your models here.
class WatchList(models.Model):
    title = models.CharField(max_length=50)
    story_line = models.TextField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name