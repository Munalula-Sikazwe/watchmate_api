from  django.urls import path
from .views import GetCreateStreamPlatformAV, GetCreateWatchListAV, GetSingleStreamPlatformAv, GetSingleWatchListAV, \
    GetCreateReview, GetSingleReview

app_name = 'watchlist'
urlpatterns = [
    path('watchlist',GetCreateWatchListAV.as_view(),name='watchlist'),
    path('stream-platform/<int:pk>',GetSingleStreamPlatformAv.as_view(),name='streamplatform-detail'),
    path('stream-platform',GetCreateStreamPlatformAV.as_view()),
    path('watchlist/<int:pk>',GetSingleWatchListAV.as_view(),name='watchlist-detail'),
    path('watchlist/<int:pk>/reviews',GetCreateReview.as_view(),name='watchlist-reviews'),
    path('watchlist/reviews/<int:pk>',GetSingleReview.as_view(),name='watchlist-reviews-detail')
]