from rest_framework.serializers import ModelSerializer

from watchlist_app.models import StreamPlatform, WatchList, Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class WatchListSerializer(ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(ModelSerializer):
    watchlist = WatchListSerializer(read_only=True, many=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
