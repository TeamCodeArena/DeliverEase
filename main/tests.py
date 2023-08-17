from django.test import TestCase, Client
from django.urls import reverse
from buyer.models import Buyer, Seller

class MainTestCase(TestCase):
    def test_index_page(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_us_page(self):
        c = Client()
        response = c.get("/about_us/")
        self.assertEqual(response.status_code, 200)

    def test_get_started_page(self):
        c = Client()
        response = c.get('/get_started/')
        self.assertEqual(response.status_code, 200)

