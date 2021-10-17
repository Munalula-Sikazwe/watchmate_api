from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from user_app.views import RegistrationView, LogoutView

app_name = 'user'
urlpatterns = [
    path('logout',LogoutView.as_view(),name='logout'),
    path('registration',RegistrationView.as_view(),name='registration'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]