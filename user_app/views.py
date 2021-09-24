# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from user_app.serializers import RegistrationSerializer


class RegistrationView(CreateAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class LogoutView(APIView):

    def post(self, request):
        if request.user.is_authenticated():
            request.user.authtoken.delete()
            return Response({"success":"You have successfully logged out."},status=status.HTTP_200_OK)
