from  django.urls import path
from .views import GetCreateStreamPlatformAV
app_name = 'watchlist'
urlpatterns = [
    path('stream-platform',GetWatchListAV.as_view(),),
    path('watchlist',GetCreateStreamPlatformAV.as_view())
]