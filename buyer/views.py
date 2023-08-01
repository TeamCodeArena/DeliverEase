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



def index(request):
    email = request.GET.get('email', 'None')
    if email == 'None':
        if 'buyer_id' in request.session:
            pass
        else:
            return HttpResponseRedirect('/auth/login')


    print(f'email: {email}')
    try:
        buyer = Buyer.objects.get(email=email)
    except:
        id = request.session['buyer_id']
        buyer = Buyer.objects.get(pk=id)
    else:
        request.session['buyer_id'] = buyer.id

    return render(request, 'buyer/buyer_homepage.html')


def add_job(request):
    if request.method == 'POST':
        id = request.session['buyer_id']
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
        try:
            delivery_pincode = int(delivery_pincode)
            pickup_pincode = int(pickup_pincode)
        except:
            return HttpResponseRedirect(reverse('add_job'))
        try:
            new_job = Job(pickup_address=pickup_address, pickup_time=pickup_time1,
                          delivery_address=delivery_address, pickup_pincode=pickup_pincode,
                          delivery_time=delivery_time1, created_by=current_buyer,
                          delivery_pincode=delivery_pincode)
        except:
            return HttpResponseRedirect(reverse('add_job'))
        else:
            print(new_job)
            new_job.save()
        return HttpResponseRedirect (reverse('my_orders'))
    elif request.method == 'GET':

        if 'buyer_id' in request.session:
            print(request.session['buyer_id'])

        else:
            return HttpResponseRedirect('/auth/login')

        return render(request, 'buyer/add_job.html')



def my_orders(request):
    if request.method == 'POST':
        job_id = request.POST['job_id']
        request.session['job_id'] = job_id
        return HttpResponseRedirect (reverse('check_order'))
    else:
        if 'buyer_id' in request.session:
            print(request.session['buyer_id'])
        else:
            return HttpResponseRedirect('/auth/login')

        try:
            del request.session['job_id']
        except:
            pass
        id = request.session['buyer_id']
        # print(id)
        buyer =  Buyer.objects.filter(id=id)
        # print(buyer)
        all_job = Job.objects.filter(created_by=id)
        return render(request, 'buyer/my_orders.html', {
            'jobs': all_job, 'buyer': buyer
        })


def check_order(request):
    if request.method == 'POST':
        return HttpResponseRedirect (reverse('get_otp'))

    if 'buyer_id' in request.session:
        pass
    else:
        return HttpResponseRedirect('/auth/login')

    try:
        job_id = request.session['job_id']
    except:
        return HttpResponseRedirect(reverse('my_orders'))
    print(job_id)
    job = Job.objects.get(pk=job_id)
    return render(request, 'buyer/check_order.html', {
        'job': job
    })


def get_otp(request):
    if request.method == 'POST':
        job_id = request.session['job_id']
        get_job = Job.objects.get(id=job_id)
        try:
            review = request.POST['review']
            rating = request.POST['rating']
            get_job.review  = review
            get_job.rating = rating
            get_job.save()
        except:
            print(get_job)
            print(review, rating)
            return HttpResponseRedirect(reverse('get_otp'))
        return render(request, 'buyer/thank_you.html')
    if 'buyer_id' in request.session:
        pass
    else:
        return HttpResponseRedirect('/auth/login')

    job_id = request.session['job_id']
    get_job = Job.objects.get(id=job_id)
    try:
        seller_id = get_job.assigned_to.id
        seller = Seller.objects.filter(pk=seller_id)

    except:
        return render(request, 'buyer/final_page.html')
    else:
        otp = random.randint(100000, 999999)
        print(otp)
        get_job.otp = otp
        get_job.save()

        print(f'job otp {get_job.otp}')
        return render(request, 'buyer/final_page.html', {
        'seller': seller,
        'otp': otp,
        'job': get_job
        }   )