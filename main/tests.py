from django.test import TestCase, Client
from django.urls import reverse
from buyer.models import Buyer, Seller

class MainTestCase(TestCase):

    def setUp(self):
        c = Client()
        s1 = Seller.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@seller",
            experience="None"
        )
        b1 = Buyer.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@buyer"
        )
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

    def test_red_home_for_seller_id(self):
        c = Client()
        session = c.session
        session["id"] = 1
        session.save()
        print("hello")
        response = c.get(reverse("redirect_home"))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_red_home_for_buyer_id(self):
        c = Client()
        session = c.session
        session["buyer_id"] = 1
        session.save()
        print("hello")
        response = c.get("/red_home/")
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("index"))

    def test_red_home_for_no_id(self):
        c = Client()
        response = c.get("/red_home/")
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))




