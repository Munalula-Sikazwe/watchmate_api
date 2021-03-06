import pdb

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from watchlist_app.models import StreamPlatform, WatchList, Review
from watchlist_app.permissions import UserPermissions, ReviewPermissions
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']



class GetSingleWatchListAV(RetrieveUpdateDestroyAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer


class GetSingleReview(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewPermissions]


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
            raise ValidationError( "You have already made a review for this watchlist.")
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            raise ValidationError( "The watchlist does not exist")
        watchlist.total_ratings += 1
        if watchlist.avg_rating == 0:
            watchlist.avg_rating = serializer.validated_data.get('rating')
        else:
            watchlist.avg_rating += serializer.validated_data.get('rating')
            watchlist.avg_rating /= 2
        watchlist.save()
        serializer.save(reviewer=reviewer,watchlist=watchlist)


class StreamPlatformVs(ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
