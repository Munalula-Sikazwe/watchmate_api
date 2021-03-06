from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from watchlist_app.models import StreamPlatform, WatchList, Review


class ReviewSerializer(ModelSerializer):


    class Meta:
        model = Review
        exclude = ('reviewer',)

class WatchListSerializer(ModelSerializer):
    reviews = StringRelatedField(many=True)



    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(ModelSerializer):
    watchlist = WatchListSerializer(read_only=True, many=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
