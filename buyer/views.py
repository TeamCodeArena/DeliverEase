from django.shortcuts import render
from userAuth.models import Buyer,  Seller
from .models import Job
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import random
from django.urls import reverse
# Create your views here.
# path('home/', views.home, name='index'),
# path('add_job/', views.add_job, name='add_job'),
# path('my_orders/', views.my_orders, name='my_orders'),
# path('check_order/', views.check_order, name='check_order')

def check_user_loggedin(request):
    try:
        id = request.session['id']
        print(id)
    except Exception as error:
        print(error)




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
    email = request.GET.get('email', 'None')
    print(f'email: {email}')
    buyer = Buyer.objects.get(email=email)
    id = buyer.id
    request.session['id'] = id
    return render(request, 'buyer/buyer_homepage.html')


def add_job(request):
    if request.method == 'POST':
        id = request.session['id']
        print(f'id {id}')
        current_buyer = Buyer.objects.get(id=id)
        pickup_address = request.POST['pickup_address']
        pickup_time1 = request.POST['pickup_time']
        pickup_date = request.POST['pickup_date']
        delivery_address = request.POST['delivery_address']
        delivery_time1 = request.POST['delivery_time']
        delivery_date = request.POST['delivery_date']
        delivery_pincode = request.POST['delivery_pincode']
        pickup_pincode = request.POST['pickup_pincode']
        new_job = Job(pickup_address=pickup_address, pickup_time=pickup_time1,
                      delivery_address=delivery_address, pickup_pincode=pickup_pincode,
                      delivery_time=delivery_time1, created_by=current_buyer,
                      delivery_pincode=delivery_pincode)
        print(new_job)
        new_job.save()
        return HttpResponseRedirect (reverse('my_orders'))

    else:
        check_user_loggedin(request=request)
        return render(request, 'buyer/add_job.html')



def my_orders(request):
    if request.method == 'POST':

        job_id = request.POST['job_id']
        request.session['job_id'] = job_id
        return HttpResponseRedirect (reverse('check_order'))

    else:
        try:
            del request.session['job_id']
        except:
            pass
        id = request.session['id']
        # print(id)
        buyer =  Buyer.objects.filter(id=id)
        # print(buyer)
        all_job = Job.objects.filter(created_by=id)

        return render(request, 'buyer/my_orders.html', {
            'jobs': all_job, 'buyer': buyer
        }) #check in vs code for different template

def check_order(request):
    if request.method == 'POST':
        return HttpResponseRedirect (reverse('get_otp'))
    job_id = request.session['job_id']
    print(job_id)
    job = Job.objects.get(pk=job_id)
    return render(request, 'buyer/check_order.html', {
        'job': job
    })


def get_otp(request):
    otp = random.randint(100000, 999999)
    print(otp)
    job_id = request.session['job_id']
    get_job = Job.objects.get(id=job_id)
    get_job.otp = otp
    get_job.save()
    print(f'job otp {get_job.otp}')
    return render(request, 'buyer/final_page.html', {
        'otp': otp
    })