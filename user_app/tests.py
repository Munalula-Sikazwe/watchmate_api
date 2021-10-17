from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_205_RESET_CONTENT
from rest_framework.test import APITestCase
from django.urls import reverse


# Create your tests here.
class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            'username': 'testusername',
            'email': 'testemail@gmail.com',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'password': 'test_password',
            'password2': 'test_password'
        }

        url = reverse('user:registration')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create_user(username='testuser', password='test_password')

    def test_login(self):
        data = {
            'username': 'testuser',
            'password': 'test_password'
        }
        url = reverse('user:token_obtain_pair')

        response = self.client.post(url, data)
        self.refresh_token = response.data.get('refresh')
        self.access_token = response.data.get('access')
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_logout(self):
        self.test_login()
        url = reverse('user:logout')
        data = {
            "token":self.refresh_token
        }
        self.client.credentials(HTTP_AUTHORIZATION = "Bearer "+self.access_token)

        response = self.client.post(url,data)
        self.assertEqual(response.status_code,HTTP_205_RESET_CONTENT)
