from rest_framework.test import APITestCase
from rest_framework import status

class HealthCheckTests(APITestCase):
    def test_health_check(self):
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)