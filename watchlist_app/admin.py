from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import WatchList, StreamPlatform, Review, MyUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    pass
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
admin.site.register(MyUser)