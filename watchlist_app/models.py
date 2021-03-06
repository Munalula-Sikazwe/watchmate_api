from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models import CASCADE

from django.conf import settings

roles = (
    ('supervisor',"SuperVisor"),
    ('sales_agent',"SalesAgent"),
    ('customer',"Customer"),
    ('director',"Director")
)
class MyUser(AbstractUser):
    user_role = models.CharField(choices=roles,max_length=100,default='customer')
    def __str__(self):
        return f'{self.username}'

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
    platform = models.ForeignKey(StreamPlatform, on_delete=CASCADE, related_name='watchlist', null=True)
    avg_rating = models.FloatField(default=0)
    total_ratings = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Review(models.Model):
    reviewer = models.ForeignKey(MyUser,on_delete=CASCADE,related_name='my_user')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating}-{self.watchlist.title}."
