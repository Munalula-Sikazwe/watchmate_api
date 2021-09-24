

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView

from user_app.serializers import RegistrationSerializer


class RegistrationView(CreateAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = RegistrationSerializer



