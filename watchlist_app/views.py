from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from watchlist_app.models import StreamPlatform, WatchList, Review
from watchlist_app.serializers import StreamPlatformSerializer, WatchListSerializer, ReviewSerializer


class GetCreateStreamPlatformAV(ListCreateAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class GetSingleStreamPlatformAv(RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class GetCreateWatchListAV(ListCreateAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class GetSingleWatchListAV(RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class GetSingleReview(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

