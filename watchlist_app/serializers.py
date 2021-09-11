from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from watchlist_app.models import StreamPlatform, WatchList


class WatchListSerializer(ModelSerializer):
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(HyperlinkedModelSerializer):


    class Meta:
        model = StreamPlatform
        fields = '__all__'
