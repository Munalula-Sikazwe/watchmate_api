
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

class RegistrationSerializer(ModelSerializer):

    password2 = CharField(max_length=100,style={"input_type": "password"},write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name','password','password2')
        extra_kwargs ={'password':{'write_only':True}}

    def save(self):
        user = get_user_model()
        password = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')

        if password != password2:
            raise ValidationError("The passwords do not match")

        account = user.objects.create(username=self.validated_data.get('username'),email=self.validated_data.get('email'),first_name=self.validated_data.get('first_name'),last_name=self.validated_data.get('last_name'))
        account.set_password(password)
        account.save()

        return account
