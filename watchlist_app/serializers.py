from rest_framework.serializers import ModelSerializer

from watchlist_app.models import StreamPlatform, WatchList


class StreamPlatformSerializer(ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'


class WatchListSerializer(WatchList):
    class Meta:
        model = WatchList
        fields = '__all__'
