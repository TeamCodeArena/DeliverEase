from django.test import TestCase, Client
from django.db.models import Max
from buyer.models import Job, Seller, Buyer
from django.urls import reverse

class RedirectingToBuyerPagesWithoutUserLogin(TestCase):
    def test_home_page(self):
        c = Client()
        response = c.get(reverse("index"))
        self.assertRedirects(response, reverse("login"))

    def test_add_job_page(self):
        c = Client()
        response = c.get(reverse("add_job"))
        self.assertRedirects(response, reverse("login"))

    def test_my_orders_page(self):
        c = Client()
        response = c.get(reverse("my_orders"))
        self.assertRedirects(response, reverse("login"))

    def test_check_order_page(self):
        c = Client()
        response = c.get(reverse("check_order"))
        self.assertRedirects(response, reverse("login"))

    def test_get_otp_page(self):
        c = Client()
        response = c.get(reverse("get_otp"))
        self.assertRedirects(response, reverse("login"))

    def test_completed_jobs_page(self):
        c = Client()
        response = c.get(reverse("buyer_completed_jobs"))
        self.assertRedirects(response, reverse("login"))

    def test_thank_you_page(self):
        c = Client()
        response = c.get(reverse("thank_you"))
        self.assertRedirects(response, reverse("login"))
#
class RedirectingToBuyerPagesWithoutJobCredentials(TestCase):
    def setUp(self):

        b1 = Buyer.objects.create(
                name="Aryan Gupta",
                password="hiaryan",
                address="ghar pr",
                phone_no="9999",
                email="aryan@buyer"
            )
        b2 = Buyer.objects.create(
                name="Aryan Gupta",
                password="hiaryan",
                address="ghar pr",
                phone_no="9999",
                email="aryan@buyer2"
            )

    def test_check_order_page(self):
        c = Client()
        session = c.session
        s1 = Buyer.objects.get(pk=2)
        session["buyer_id"] = s1.id
        session.save()
        response = c.get(reverse("check_order"))
        self.assertRedirects(response, reverse("my_orders"))

    def test_get_otp_page(self):
        c = Client()
        session = c.session
        s1 = Buyer.objects.get(pk=2)
        session["buyer_id"] = s1.id
        session.save()
        response = c.get(reverse("get_otp"))
        self.assertRedirects(response, reverse("my_orders"))


#
class BuyerTestCase(TestCase):
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
        s2 = Seller.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@new_seller",
            experience="None"
        )
        s3 = Seller.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@new_seller2",
            experience="None"
        )
        s4 = Seller.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@new_seller2003",
            experience="None"
        )
        s5 = Seller.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@new_seller200331",
            experience="None"
        )
        b1 = Buyer.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@buyer"
        )
        b2 = Buyer.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@buyer2"
        )
        b3 = Buyer.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@buyer3"
        )
        b4 = Buyer.objects.create(
            name="Aryan Gupta",
            password="hiaryan",
            address="ghar pr",
            phone_no="9999",
            email="aryan@buyer4"
        )

        job1 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=14234,
            pickup_pincode=23453,
            created_by=b1,
            assigned_to=s1,
            status="In Progress",
            delivery_date="12 August",
            pickup_date="10 August"
        )

        # unassigned job
        job2 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=14234,
            pickup_pincode=23453,
            created_by=b1,
            delivery_date="12 August",
            pickup_date="10 August"
        )

        job3 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=14234,
            pickup_pincode=23453,
            created_by=b2,
            assigned_to=s2,
            status="In Progress",
            delivery_date="12 August",
            pickup_date="10 August"
        )
        job4 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=14234,
            pickup_pincode=23453,
            created_by=b2,
            assigned_to=s4,
            status="In Progress",
            delivery_date="12 August",
            pickup_date="10 August"
        )
        job5 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=242234,
            pickup_pincode=23432453,
            created_by=b1,
            assigned_to=s4,
            status="In Progress",
            delivery_date="12 August",
            pickup_date="10 August"
        )
        job6 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=242234,
            pickup_pincode=23432453,
            created_by=b1,
            assigned_to=s5,
            status="Completed",
            delivery_date="12 August",
            pickup_date="10 August"
        )
        job7 = Job.objects.create(
            pickup_address="home",
            delivery_address="office",
            delivery_time="5pm",
            pickup_time="10pm",
            delivery_pincode=14234,
            pickup_pincode=23453,
            created_by=b4,
            assigned_to=s1,
            status="In Progress",
            delivery_date="12 August",
            pickup_date="10 August"
        )
    def test_home_page_redirect_from_other_page(self):
        c = Client()

        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()

        response = c.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "buyer/buyer_homepage.html")


    def test_add_job_page_get_request(self):
        c = Client()
        response = c.get(f"{reverse('index')}?email=aryan@buyer")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "buyer/buyer_homepage.html")

    def test_add_job_page_post_request_valid_job(self):
        c = Client()

        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        data = {
            "pickup_address": "ghar se",
            "pickup_time": "7 pm",
            "pickup_date": "12 July",
            "delivery_address": "tere ghar pr",
            "delivery_time": "4 pm",
            "delivery_date": "15 July",
            "delivery_pincode": 432423,
            "pickup_pincode": 32432
        }
        response = c.post(reverse("add_job"), data)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Job.objects.count(), 8)
        self.assertRedirects(response, reverse("my_orders"))
    def test_add_job_page_post_request_invalid_job(self):
        c = Client()

        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        data = {
            "pickup_address": "ghar se",
            "pickup_time": "7 pm",
            "pickup_date": "12 July",
            "delivery_address": "tere ghar pr",
            "delivery_time": "4 pm",
            "delivery_date": "15 July",
            "delivery_pincode": "432f423",
            "pickup_pincode": "3243f2"
        }
        response = c.post(reverse("add_job"), data)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("add_job"))
    def test_add_job_page_post_request_incomplete_job(self):
        c = Client()

        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        data = {
            "pickup_address": "ghar se",
            "pickup_time": "7 pm",
            "pickup_date": "12 July",
            "delivery_address": "tere ghar pr",
            "delivery_date": "15 July",
            "delivery_pincode": "432f423",
            "pickup_pincode": "3243f2"
        }
        response = c.post(reverse("add_job"), data)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Job.objects.count(), 7)
        self.assertRedirects(response, reverse("add_job"))

    def test_my_orders_page_without_jobs_get_request(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=3)

        session["buyer_id"] = b1.id
        session.save()
        response = c.get(reverse("my_orders"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context["jobs"].count(), 0)
        self.assertTemplateUsed(response, "buyer/my_orders.html")

    def test_my_orders_page_with_multiple_jobs_get_request(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=1)

        session["buyer_id"] = b1.id
        session.save()
        response = c.get(reverse("my_orders"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context["jobs"].count(), 4)
        self.assertTemplateUsed(response, "buyer/my_orders.html")

    def test_my_orders_page_with_one_job_get_request(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=4)

        session["buyer_id"] = b1.id
        session.save()
        response = c.get(reverse("my_orders"))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context["jobs"].count(), 1)
        self.assertTemplateUsed(response, "buyer/my_orders.html")

    def test_job_check_order_page_get_method(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        job1 = Job.objects.get(pk=1)
        session["job_id"] = job1.id
        session.save()
        response = c.get(reverse("check_order"))
        self.assertTemplateUsed(response, "buyer/check_order.html")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context["job"], job1)

    def test_job_otp_page_with_assigned_job(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        job1 = Job.objects.get(pk=1)
        session["job_id"] = job1.id
        session.save()
        response = c.get(reverse("get_otp"))
        self.assertTemplateUsed(response, "buyer/final_page.html")
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context["job"], job1)
    def test_job_otp_page_with_unassigned_job(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        job1 = Job.objects.get(pk=2)
        session["job_id"] = job1.id
        session.save()
        response = c.get(reverse("get_otp"))
        self.assertTemplateUsed(response, "buyer/final_page.html")
        self.assertEquals(response.status_code, 200)

    def test_completed_orders_with_zero_completed_jobs(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=2)
        jobs = Job.objects.filter(created_by=b1, status="Completed")
        session["buyer_id"] = b1.id
        session.save()
        response = c.get(reverse("buyer_completed_jobs"))
        self.assertTemplateUsed(response, "buyer/buyer_completed_jobs.html")
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context["jobs"], jobs)
    def test_completed_orders_with_a_completed_job(self):
        c = Client()
        session = c.session
        b1 = Buyer.objects.get(pk=1)
        session["buyer_id"] = b1.id
        session.save()
        job1 = Job.objects.filter(created_by=b1, status="Completed")
        response = c.get(reverse("buyer_completed_jobs"))
        self.assertTemplateUsed(response, "buyer/buyer_completed_jobs.html")
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context["jobs"], job1)
