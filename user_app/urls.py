from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user_app.views import RegistrationView

app_name = 'user'
urlpatterns = [
    path('login',obtain_auth_token,name='login'),
    path('registration',RegistrationView.as_view(),name='registration'),
]