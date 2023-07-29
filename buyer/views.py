from django.shortcuts import render
from userAuth.models import Buyer,  Seller
from .models import Job
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
# path('home/', views.home, name='index'),
# path('add_job/', views.add_job, name='add_job'),
# path('my_orders/', views.my_orders, name='my_orders'),
# path('check_order/', views.check_order, name='check_order')


def assign_job(order_tag, seller_id, buyer_email):

    buyer = Buyer.query.filter_by(email=buyer_email).first()
    print('Buyer', buyer)
    buyer_id = buyer.id
    print('Buyer ID', buyer_id)
    buyer_job = Job.query.filter_by(created_by=buyer_id, assigned_to=0).filter_by(
        order_tag=order_tag).first() ##checks if the job is available
    # print('Job', buyer_job)
    if buyer_job:
        buyer_job.assigned_to = seller_id
        db.session.commit()
        buyer_job.status = "In Progress"
        db.session.commit()
        print('Job Assigned')
    else:
        print('Job already assigned to someone')


def cancel_job(job_id, seller_id, buyer_email):
    buyer = Buyer.objects.filter(email=buyer_email)
    print('Buyer', buyer)
    buyer_id = buyer.id
    print('Buyer ID', buyer_id)
    buyer_job = Job.objects.filter(created_by=buyer_id, assigned_to=seller_id, id=job_id)
    ##checks if the job is available
    # print('Job', buyer_job)
    if buyer_job:
        buyer_job.assigned_to = 0
        buyer_job.save()
        buyer_job.status = "Cancelled"
        buyer_job.save()
        print('Job Cancelled Success')
    else:
        print('Job not  assigned to you')


def display_jobs():
    number_of_jobs = Job.objects.count()
    if number_of_jobs < 5:
        jobs = Job.objects.filter(assigned_to=0).order_by(func.random()).limit(number_of_jobs).all()
    else:
        jobs = Job.query.filter_by(assigned_to=0).order_by(func.random()).limit(5).all()
    # Print the job details
    for job in jobs:
        print(job)


def order_completed(job_id, seller_id, buyer_email, rating):
    buyer = Buyer.objects.get(email=buyer_email)
    print('Buyer', buyer)
    buyer_id = buyer.id
    print('Buyer ID', buyer_id)

    buyer_job = Job.objects.filter(created_by=buyer_id, assigned_to=seller_id, status='In Progress')
    if buyer_job:
        print(buyer_job)
        buyer_job.status = 'Completed'
        db.session.commit()
        buyer_job.rating = rating
        db.session.commit()
        print('Order Completed Successfully')
        print(buyer_job)
    else:
        print('Error')

def get_reviews(seller_id):
    seller_reviews = Job.objects.filter(assigned_to=seller_id, status='Completed').all()
    for seller_review in seller_reviews:
        print(seller_review.rating)
        print(seller_review.review)


def index(request):

    return render(request, 'buyer/buyer_homepage.html')

@login_required(login_url='/auth/login')
def add_job(request):
    if request.method == 'POST':
        pickup_address = request.POST['pickup_address']
        pickup_time1 = request.POST['pickup_time']
        pickup_date = request.POST['pickup_date']
        delivery_address = request.POST['delivery_address']
        delivery_time1 = request.POST['delivery_time']
        delivery_date = request.POST['delivery_date']
        delivery_pincode = request.POST['delivery_pincode']
        pickup_pincode = request.POST['pickup_pincode']
        product_type = request.POST['product_type']
    else:

        author = request.user
        print(f'author {author}')
        return render(request, 'buyer/add_job.html')



def my_orders(request):
    return render(request, 'buyer/buyer_orders.html') #check in vs code for different template

def check_order(request):
    return render(request, 'buyer/check_order.html')