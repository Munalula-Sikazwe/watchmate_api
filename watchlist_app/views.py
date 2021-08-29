from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
# Create your views here.
from watchlist_app.models import StreamPlatform, WatchList
from watchlist_app.serializers import StreamPlatformSerializer, WatchListSerializer


class GetCreateStreamPlatformAV(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
class GetCreateWatchListAV(ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

