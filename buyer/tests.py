from django.test import TestCase, Client
from django.db.models import Max
from buyer.models import Job, Seller, Buyer
from django.urls import reverse

class RedirectingToBuyerPagesWithoutUserLogin(TestCase):
    def test_home(self):
        c = Client()
        response = c.get(reverse("index"))
        self.assertRedirects(response, reverse("login"))

    def test_job_details(self):
        c = Client()
        response = c.get(reverse("add_job"))
        self.assertRedirects(response, reverse("login"))

    def my_orders(self):
        c = Client()
        response = c.get(reverse("my_orders"))
        self.assertRedirects(response, reverse("login"))

    def completed_jobs(self):
        c = Client()
        response = c.get(reverse("check_order"))
        self.assertRedirects(response, reverse("login"))

    def complete_delivery(self):
        c = Client()
        response = c.get(reverse("get_otp"))
        self.assertRedirects(response, reverse("login"))

    def complete_delivery(self):
        c = Client()
        response = c.get(reverse("buyer_completed_jobs"))
        self.assertRedirects(response, reverse("login"))

    def complete_delivery(self):
        c = Client()
        response = c.get(reverse("thank_you"))
        self.assertRedirects(response, reverse("login"))
#
# class RedirectingWithoutJobCredentials(TestCase):
#     def test_job_details(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         response = c.get(reverse("job_details"))
#         self.assertRedirects(response, reverse("seller_orders"))
#
#     def test_complete_delivery_get_method(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         response = c.get(reverse("complete_delivery"))
#         self.assertRedirects(response, reverse("seller_orders"))
#
#
#
# class SellerTestCase(TestCase):
#     def setUp(self):
#         c = Client()
#         s1 = Seller.objects.create(
#             name="Aryan Gupta",
#             password="hiaryan",
#             address="ghar pr",
#             phone_no="9999",
#             email="aryan@seller",
#             experience="None"
#         )
#         s2 = Seller.objects.create(
#             name="Aryan Gupta",
#             password="hiaryan",
#             address="ghar pr",
#             phone_no="9999",
#             email="aryan@new_seller",
#             experience="None"
#         )
#         s3 = Seller.objects.create(
#             name="Aryan Gupta",
#             password="hiaryan",
#             address="ghar pr",
#             phone_no="9999",
#             email="aryan@new_seller2",
#             experience="None"
#         )
#         s4 = Seller.objects.create(
#             name="Aryan Gupta",
#             password="hiaryan",
#             address="ghar pr",
#             phone_no="9999",
#             email="aryan@new_seller2003",
#             experience="None"
#         )
#         s5 = Seller.objects.create(
#             name="Aryan Gupta",
#             password="hiaryan",
#             address="ghar pr",
#             phone_no="9999",
#             email="aryan@new_seller200331",
#             experience="None"
#         )
#         b1 = Buyer.objects.create(
#             name="Aryan Gupta",
#             password="hiaryan",
#             address="ghar pr",
#             phone_no="9999",
#             email="aryan@buyer"
#         )
#
#         job1 = Job.objects.create(
#             pickup_address="home",
#             delivery_address="office",
#             delivery_time="5pm",
#             pickup_time="10pm",
#             delivery_pincode=14234,
#             pickup_pincode=23453,
#             created_by=b1,
#             assigned_to=s1,
#             status="In Progress"
#         )
#
#         # unassigned job
#         job2 = Job.objects.create(
#             pickup_address="home",
#             delivery_address="office",
#             delivery_time="5pm",
#             pickup_time="10pm",
#             delivery_pincode=14234,
#             pickup_pincode=23453,
#             created_by=b1
#         )
#
#         job3 = Job.objects.create(
#             pickup_address="home",
#             delivery_address="office",
#             delivery_time="5pm",
#             pickup_time="10pm",
#             delivery_pincode=14234,
#             pickup_pincode=23453,
#             created_by=b1,
#             assigned_to=s2,
#             status="In Progress"
#         )
#         job3 = Job.objects.create(
#             pickup_address="home",
#             delivery_address="office",
#             delivery_time="5pm",
#             pickup_time="10pm",
#             delivery_pincode=14234,
#             pickup_pincode=23453,
#             created_by=b1,
#             assigned_to=s4,
#             status="In Progress"
#         )
#         job4 = Job.objects.create(
#             pickup_address="home",
#             delivery_address="office",
#             delivery_time="5pm",
#             pickup_time="10pm",
#             delivery_pincode=242234,
#             pickup_pincode=23432453,
#             created_by=b1,
#             assigned_to=s4,
#             status="In Progress"
#         )
#         job5 = Job.objects.create(
#             pickup_address="home",
#             delivery_address="office",
#             delivery_time="5pm",
#             pickup_time="10pm",
#             delivery_pincode=242234,
#             pickup_pincode=23432453,
#             created_by=b1,
#             assigned_to=s5,
#             status="Completed"
#         )
#     def test_home_page_redirect_from_other_page(self):
#         c = Client()
#
#         session = c.session
#         s1 = Seller.objects.get(pk=1)
#         session["id"] = s1.id
#         session.save()
#
#         response = c.get(reverse("home"))
#
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(response.context["jobs"].count(), 1)
#         self.assertTemplateUsed(response, "seller/jobs.html")
#
#
#     def test_home_page_get(self):
#         c = Client()
#         response2 = c.get(f"{reverse('home')}?email=aryan@seller")
#
#         self.assertEquals(response2.status_code, 200)
#         self.assertEquals(response2.context["jobs"].count(), 1)
#         self.assertTemplateUsed(response2, "seller/jobs.html")
#
#     def test_my_orders_page_without_jobs(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=3)
#
#         session["id"] = s1.id
#         session.save()
#         response = c.get(reverse("seller_orders"))
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(response.context["jobs"].count(), 0)
#         self.assertTemplateUsed(response, "seller/myOrder.html")
#
#     def test_my_orders_page_with_a_job(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         response = c.get(reverse("seller_orders"))
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(response.context["jobs"].count(), 1)
#         self.assertTemplateUsed(response, "seller/myOrder.html")
#     def test_my_orders_page_with_many_jobs(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=4)
#         session["id"] = s1.id
#         session.save()
#         response = c.get(reverse("seller_orders"))
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(response.context["jobs"].count(), 2)
#         self.assertTemplateUsed(response, "seller/myOrder.html")
#
#     def test_my_orders_page_with_post_request(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         job1 = Job.objects.get(pk=3)
#         post_response = c.post(reverse("seller_orders"), {"job_id": job1.id})
#         self.assertEquals(post_response.status_code, 302)
#         self.assertRedirects(post_response, reverse("complete_delivery"))
#
#     def test_job_details_page_get(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         job1 = Job.objects.get(pk=2)
#         session["job_id"] = job1.id
#         session.save()
#         response = c.get(reverse("job_details"))
#         self.assertTemplateUsed(response, "seller/sellerEachjobpage.html")
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(response.context["job"], job1)
#
#     def test_job_details_page_post(self):
#        c = Client()
#        session = c.session
#        s1 = Seller.objects.get(pk=2)
#        session["id"] = s1.id
#        session.save()
#        job1 = Job.objects.get(pk=2)
#        session["job_id"] = job1.id
#        session.save()
#        response = c.post(reverse("job_details"))
#        self.assertRedirects(response, reverse("complete_delivery"))
#        self.assertEquals(response.status_code, 302)
#
#     def test_complete_delivery_page_get(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         job1 = Job.objects.get(pk=2)
#         session["job_id"] = job1.id
#         session.save()
#         response = c.get(reverse("complete_delivery"))
#         self.assertTemplateUsed(response, "seller/seller_finish_delivery.html")
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(response.context["job"], job1)
#
#     def test_complete_delivery_page_postReq_without_int_otp(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=2)
#         session["id"] = s1.id
#         session.save()
#         job1 = Job.objects.get(pk=1)
#         session["job_id"] = job1.id
#         session.save()
#         response = c.post(reverse("complete_delivery"), {"otp": "2342234"})
#         self.assertEquals(response.status_code, 200)
#
#
#     def test_completed_jobs_get(self):
#         c = Client()
#         session = c.session
#         s1 = Seller.objects.get(pk=5)
#         session["id"] = s1.id
#         session.save()
#         job1 = Job.objects.get(pk=5)
#         session["job_id"] = job1.id
#         session.save()
#         response = c.get(reverse("completed_jobs"))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, "seller/reviews.html")
