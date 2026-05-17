from django.test import TestCase
from rest_framework.test import APIClient
from datetime import date, timedelta
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.

class ConsultaTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='teste_user', password='senha_incorreta')
        self.client.force_authenticate(user=self.user)

    
    def teste_data_invalida(self):
        data_passada = date.today() - timedelta(days=1)
        data = {
            "data":data_passada,
            "hora":"14:00",
            "medico":"Dr. João",
            "especialidade":"Ortopedista",
            "localizacao":"Ala 9, predio B"
        }

        response = self.client.post('/api/consultas/', data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('data', response.data)
    