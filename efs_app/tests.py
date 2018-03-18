from django.test import TestCase
import requests
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Investment, Stock, Customer
# Create your tests here.
class EfsAppAPITests(APITestCase):
    
    def test_customer_api_if_its_available(self):
        # client = RequestsClient()
        url = ('/customers_json/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  

    def test_investment_api_if_its_available(self):
        # client = RequestsClient()
        url = ('/investments_json/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_stock_api_if_its_available(self):
        # client = RequestsClient()
        url = ('/stocks_json/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_investment_api_if_its_available(self):
        # client = RequestsClient()
        url = ('/1/investments_json/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

