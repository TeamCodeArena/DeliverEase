from django.shortcuts import render
from buyer.models import Buyer, Seller, Job
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.


def home(request):

    if request.method == 'POST':
        job_id = request.POST['job_id']
        request.session['job_id'] = job_id
        print('hi')
        return HttpResponseRedirect (reverse('job_details'))

    elif request.method == 'GET':
        email = request.GET.get('email', 'None')
        if  email == 'None':
            return HttpResponseRedirect('/auth/login')
        print(email)
        seller = Seller.objects.get(email=email)
        request.session['id'] = seller.id

        jobs = Job.objects.filter(assigned_to__isnull=True)
            # buyer

        return render(request, 'seller/jobs.html',{
            'jobs': jobs
        })


# def jobs(request):
#     return render(request, 'seller/jobs.html')
def logout(request):

    return

def my_orders(request):
    if request.method == 'POST':

        job_id = request.POST['job_id']
        request.session['job_id'] = job_id
        return HttpResponseRedirect (reverse('job_details'))
    if 'id' in request.session:
        pass
    else:
        return HttpResponseRedirect('/auth/login')

    id = request.session['id']
    current_user = Seller.objects.get(pk=id)
    jobs = Job.objects.filter(assigned_to=current_user)
    for job in jobs:
        print(f'posted by: {job.created_by.name}')
    return render(request, 'seller/myOrder.html',
                  {'jobs': jobs})

def job_details(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('complete_delivery'))
    if 'id' in request.session:
        pass
    else:
        return HttpResponseRedirect('/auth/login')

    print('hi')
    job_id = request.session['job_id']
    print(job_id)
    job = Job.objects.get(pk=job_id)
    return render(request, 'seller/sellerEachjobpage.html', {
        'job': job
    })



def complete_delivery(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        job_id = request.session['job_id']
        job = Job.objects.get(pk=job_id)
        if job.otp is None:
            message = 'Please ask the Buyer to generate to check the order status and generate otp'
        if job.otp:
            if (int(otp) == job.otp):
                print('here')
                job.status = 'Completed'

                job.save()
                print(job.status)
            else:
                message = 'Wrong OTP entered'
                return render(request, 'seller/seller_finish_delivery.html', {
                    'job': job
                })

    # return render(request, 'seller/sellerEachjobpage.html', {
    #     'job': job
    # })

    if 'id' in request.session:
        pass
    else:
        return HttpResponseRedirect('/auth/login')

    job_id = request.session['job_id']
    id = request.session['id']
    job = Job.objects.get(pk=job_id)
    current_seller = Seller.objects.get(pk=id)

    job.assigned_to = current_seller
    job.status = 'In Progress'
    job.save()
    job.save()
    return render(request, 'seller/seller_finish_delivery.html', {
        'job': job
    })

