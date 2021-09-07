from  django.urls import path
from .views import GetCreateStreamPlatformAV, GetCreateWatchListAV, GetSingleStreamPlatformAv

app_name = 'watchlist'
urlpatterns = [
    path('stream-platform',GetCreateWatchListAV.as_view(),),
    path('stream-platform/<int:pk>',GetSingleStreamPlatformAv.as_view(),),
    path('watchlist',GetCreateStreamPlatformAV.as_view())
]