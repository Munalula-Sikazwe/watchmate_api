# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from user_app.serializers import RegistrationSerializer, TokenBlacklistSerializer


class RegistrationView(CreateAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]


class LogoutView(GenericAPIView):
    serializer_class = TokenBlacklistSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data.get('token')
        print(token)
        refresh_token = RefreshToken(token)
        refresh_token.blacklist()
        return Response({"success":"You have successfully logged out."},status=status.HTTP_205_RESET_CONTENT)

