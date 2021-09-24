from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

class RegistrationSerializer(ModelSerializer):

    password2 = CharField(max_length=100,style={"input_type": "password"},write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password','password2')
        extra_kwargs ={'password':{'write_only':True}}