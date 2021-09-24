from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from rest_framework.authtoken.models import Token

users = get_user_model()

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

post_save.connect(create_auth_token,sender=settings.AUTH_USER_MODEL)