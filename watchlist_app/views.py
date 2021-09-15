from requests import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from rest_framework.viewsets import ModelViewSet

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

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        reviewer = self.request.user
        queryset = self.queryset.filter(watchlist=pk, reviewer=reviewer)
        if queryset.exists():
            return Response({"error": "You have already made a review for this watchlist."},
                            status=status.HTTP_409_CONFLICT)
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": "The watchlist does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer.save(reviewer=reviewer,watchlist=watchlist)


class StreamPlatformVs(ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
