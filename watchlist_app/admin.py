from django.contrib import admin
from .models import WatchList, StreamPlatform, Review, MyUser

# Register your models here.

admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(MyUser)