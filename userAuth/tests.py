from django.test import TestCase, Client
from .models import Buyer, Seller
from django.urls import reverse

class UserAuthTestCase(TestCase):
    def test_seller_signup_page(self):
        c = Client()
        response = c.get(reverse("seller_signup"))
        self.assertEqual(response.status_code, 200)
    def test_buyer_signup_page(self):
        c = Client()
        response = c.get(reverse("buyer_signup"))
        self.assertEqual(response.status_code, 200)
    def test_login_page(self):
        c = Client()
        response = c.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
class BuyerAuthTestCase(TestCase):
    def setUp(self):
        # Create Buyer and Seller
        b1 = Buyer.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@buyer"
            )

    def test_buyer_signup_page_on_correct_info(self):
        c = Client()
        data = {
            'fullName': 'John Doe',
            'email': 'john@example.com',
            'password': 'securepassword',
            'conf_password': 'securepassword',
            'phone_no': '1234567890',
            'address': '123 Main St'
        }

        # Send a POST request to the sign-up endpoint
        response = c.post(reverse("buyer_signup"), data)

        # Check the response status code
        self.assertEqual(response.status_code, 302)
        # Check the redirection link
        self.assertRedirects(response, f"{reverse('index')}?email={data['email']}")

        # Check if a new Buyer instance was created in the database
        self.assertEqual(Buyer.objects.count(), 2)

        buyer = Buyer.objects.get(email='john@example.com')

        # Check if the buyer's attributes match the data sent in the POST request
        self.assertEqual(buyer.name, 'John Doe')
        self.assertEqual(buyer.email, 'john@example.com')
        self.assertEqual(buyer.password, 'securepassword')
        self.assertEqual(buyer.phone_no, '1234567890')
        self.assertEqual(buyer.address, '123 Main St')

    def test_buyer_page_on_already_registered_email(self):
        c = Client()
        data2 = {
            'fullName': 'John Doe',
            'email': 'aryan@buyer',
            'password': 'securepassword',
            'conf_password': 'securepassword',
            'phone_no': '1234567890',
            'address': '123 Main St'
        }

        response2 = c.post(reverse("buyer_signup"), data2)

        self.assertEqual(response2.status_code, 302)
        self.assertEqual(Buyer.objects.count(), 1)
        self.assertRedirects(response2, reverse("login"))

    def test_buyer_signup_on_unequal_passwords(self):
        c = Client()

        data3 = {
            'fullName': 'John Doe',
            'email': 'aryan@new_buyer.com',
            'password': 'securepassword2',
            'conf_password': 'securepassword',
            'phone_no': '1234567890',
            'address': '123 Main St'
        }

        response3 = c.post(reverse("buyer_signup"), data3)

        self.assertEqual(response3.status_code, 302)
        self.assertEqual(Buyer.objects.count(), 1)
        self.assertRedirects(response3, reverse("buyer_signup"))

class SellerAuthTestCase(TestCase):
    def setUp(self):
        # Create Buyer and Seller
        s1 = Seller.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@seller",
            experience="None"
            )

    def test_seller_signup_page_on_correct_info(self):
        c = Client()
        data = {
            "fullName": "John Doe",
            "email": "john@example.com",
            "password": "securepassword",
            "conf_password": "securepassword",
            "phone_no": "1234567890",
            "address": "123 Main St",
            "work_experience": "None"
        }

        # Send a POST request to the sign-up endpoint
        response = c.post(reverse("seller_signup"), data)

        # Check the response status code
        self.assertEqual(response.status_code, 302)
        # Check the redirection link
        self.assertRedirects(response, f"{reverse('home')}?email={data['email']}")

        # Check if a new Buyer instance was created in the database
        self.assertEqual(Seller.objects.count(), 2)

        seller = Seller.objects.get(email='john@example.com')

        # Check if the buyer's attributes match the data sent in the POST request
        self.assertEqual(seller.name, 'John Doe')
        self.assertEqual(seller.email, 'john@example.com')
        self.assertEqual(seller.password, 'securepassword')
        self.assertEqual(seller.phone_no, '1234567890')
        self.assertEqual(seller.address, '123 Main St')
        self.assertEqual(seller.experience, 'None')

    def test_buyer_page_on_already_registered_email(self):
        c = Client()
        data2 = {
            "fullName": "John Doe",
            "email": "aryan@seller",
            "password": "securepassword",
            "conf_password": "securepassword",
            "phone_no": "1234567890",
            "address": "123 Main St",
            "work_experience": "None"
        }

        response2 = c.post(reverse("seller_signup"), data2)

        self.assertEqual(response2.status_code, 302)
        self.assertEqual(Seller.objects.count(), 1)
        self.assertRedirects(response2, reverse("login"))

    def test_buyer_signup_on_unequal_passwords(self):
        c = Client()

        data3 = {
            "fullName": "John Doe",
            "email": "aryan@new_seller.com",
            "password": "securepassword2",
            "conf_password": "securepassword",
            "phone_no": "1234567890",
            "address": "123 Main St",
            "work_experience": "None"
        }

        response3 = c.post(reverse("seller_signup"), data3)

        self.assertEqual(response3.status_code, 302)
        self.assertEqual(Seller.objects.count(), 1)
        self.assertRedirects(response3, reverse("seller_signup"))


class UserLoginTestCase(TestCase):
    def setUp(self):
        # Create Buyer and Seller
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

    def test_buyer_login(self):
        c = Client()
        data = {
            "email": "aryan@buyer",
            "password": "hiaryan"
        }
        response = c.post(reverse("login"), data)
        self.assertRedirects(response, f"{reverse('index')}?email={data['email']}")

    def test_seller_login(self):
        c = Client()
        data = {
            "email": "aryan@seller",
            "password": "hiaryan"
        }
        response = c.post(reverse("login"), data)
        self.assertRedirects(response, f"{reverse('home')}?email={data['email']}")
    def test_seller_login_wrong_pass(self):
        c = Client()
        data = {
            "email": "aryan@seller",
            "password": "hiaryan2"
        }
        response = c.post(reverse("login"), data)
        self.assertRedirects(response, reverse('login'))
    def test_buyer_login_wrong_pass(self):
        c = Client()
        data = {
            "email": "aryan@buyer",
            "password": "hiaryan2"
        }
        response = c.post(reverse("login"), data)

        self.assertRedirects(response, reverse('login'))
    def test_buyer_login_wrong_pass(self):
            c = Client()
            data = {
                "email": "aryan@buyer",
                "password": "hiaryan2"
            }
            response = c.post(reverse("login"), data)
            self.assertRedirects(response, reverse('login'))

