from django.shortcuts import render
from buyer.models import Buyer, Seller, Job
# Create your views here.

def home(request):
    email = request.GET.get('email', 'None')
    print(f'email {email}')
    seller = Seller.objects.get(email=email)
    request.session['id'] = seller.id
    no_of_jobs = Job.objects.count()
    if no_of_jobs > 5:
        jobs = Job.objects.filter(status='Pending')[:5]
    else:
        jobs = Job.objects.all()
    for job in jobs:
        print(f'posted by: {job.created_by.name}')
        # buyer

    return render(request, 'seller/jobs.html',{
        'jobs': jobs
    })

# def jobs(request):
#     return render(request, 'seller/jobs.html')

def my_orders(request):
    if request.method == 'POST':

        job_id = request.POST['job_id']
        request.session['job_id'] = job_id
        return HttpResponseRedirect (reverse('job_details'))

    id = request.session['id']
    no_of_jobs = Job.objects.filter(assigned_to=id).count()
    print(no_of_jobs)
    if no_of_jobs > 5:
        jobs = Job.objects.filter(status='Completed')[:5]
    else:
        jobs = Job.objects.all()
    for job in jobs:
        print(f'posted by: {job.created_by.name}')
    return render(request, 'seller/myOrder.html')

def job_details(request):
    job_id = request.session['job_id']
    print(job_id)
    job = Job.objects.get(pk=job_id)
    return render(request, 'seller/sellerEachjobpage.html', {
        'job': job
    })

def complete_delivery(request):

    job_id = request.session['job_id']
    id = request.session['id']
    job = Job.objects.get(pk=job_id)
    current_seller = Seller.objects.get(pk=id)

    job.assigned_to = current_seller
    job.save()
    job.status = 'In Progress'
    job.save()
    return render(request, 'seller/seller_finish_delivery.html')

