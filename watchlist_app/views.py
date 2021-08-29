from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView
# Create your views here.
from watchlist_app.models import StreamPlatform


class GetCreateStreamPlatformAV(RetrieveUpdateAPIView):
    queryset = StreamPlatform.objects.all()
    
