from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'login'
urlpatterns = [
    path('login',obtain_auth_token,name='login')
]