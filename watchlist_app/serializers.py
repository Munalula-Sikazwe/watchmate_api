from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from watchlist_app.models import StreamPlatform, WatchList, Review


class ReviewSerializer(ModelSerializer):
    depth = 2

    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(ModelSerializer):
    reviews = StringRelatedField(many=True)
    depth = 2


    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(ModelSerializer):
    watchlist = WatchListSerializer(read_only=True, many=True)
    depth = 2
    class Meta:
        model = StreamPlatform
        fields = '__all__'
