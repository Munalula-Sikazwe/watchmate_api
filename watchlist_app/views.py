
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,GenericAPIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

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


class GetCreateReview(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(watchlist=self.kwargs.get('pk'))

class StreamPlatformVs(ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer



