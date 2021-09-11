from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from watchlist_app.models import StreamPlatform, WatchList


class WatchListSerializer(ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(ModelSerializer):
    watchlist = HyperlinkedRelatedField(many=True, read_only=True, view_name='watchlist-detail')

    class Meta:
        model = StreamPlatform
        fields = '__all__'
