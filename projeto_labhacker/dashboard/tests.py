from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

class AuthTest(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_login_url(self):
        # Issue a GET request.
        response = self.client.get('/dashboard/', follow=True)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)