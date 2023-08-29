"""This module contains the seller views."""
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from buyer.models import Seller, Job


def home(request):
    """
    Allow the seller to visit the home page via 2 methods.

    1) GET : The seller is shown all the available jobs currently
    2) POST : The job_id of the job the seller wants to check out is saved in
    the session so that the job details be rendered accordingly
    """
    if request.method == "POST":
        job_id = request.POST["job_id"]
        request.session["job_id"] = job_id
        return HttpResponseRedirect(
            reverse("job_details")
        )  # redirects the user to a different url

    elif request.method == "GET":
        # This retrieves the email id of the user passed via GET request
        email = request.GET.get("email", "None")

        # The code below makes sure the user is logged in the session
        if email == "None":
            if "id" in request.session:
                print(request.session["id"])
                pass
            else:
                return HttpResponseRedirect("/auth/login/")

        #  This  code tries to search for the user with the email and saves
        #  his id in the session
        # so that the seller id is accessible in all the pages
        try:
            seller = Seller.objects.get(email=email)
        except Exception:
            id = request.session["id"]
            seller = Seller.objects.get(pk=id)
        else:
            request.session["id"] = seller.id

        # to get all the jobs which are not assigned to anyone
        jobs = Job.objects.filter(assigned_to__isnull=True)

        return render(request, "seller/jobs.html", {"jobs": jobs})


def my_orders(request):
    """
    Allow the seller to visit the  page via 2 methods.

    1) GET : The seller is shown all the jobs assigned to him and currently
    in progress.
    2) POST : The job_id of the job the seller wants to check out is saved in
    the session so that the job details be rendered accordingly
    """
    # The code is executed on a post request from the seller it searches
    # for the job and redirect the seller to the  next page accordingly
    if request.method == "POST":
        job_id = request.POST["job_id"]
        request.session["job_id"] = job_id
        job = Job.objects.get(pk=job_id)
        if job.status is None:
            return HttpResponseRedirect(reverse("job_details"))
        elif job.status == "In Progress":
            return HttpResponseRedirect(reverse("complete_delivery"))

    if "id" in request.session:
        print(request.session["id"])
    else:
        return HttpResponseRedirect("/auth/login/")

    # The code executed when the seller visits it with a GET request
    try:
        del request.session["job_id"]  # to delete the job id stored currently
        # so that a new one can be stored
    except Exception:
        pass

    id = request.session["id"]  # get the id of the current
    # seller in the session
    current_user = Seller.objects.get(pk=id)
    jobs = Job.objects.filter(
        assigned_to=current_user, status="In Progress"
    )  # get all the jobs assigned to him
    for job in jobs:
        print(
            f"posted by: {job.created_by.name}"
        )  # print the names of the buyers who created those jobs
    return render(request, "seller/myOrder.html", {"jobs": jobs})


def job_details(request):
    """
    Allow the seller to visit the  page via 2 methods.

    1) GET : The seller is the shown the details of the job he wishes to see
    2) POST : The seller is redirected to another page
    """
    # This is executed on a post request to the page
    if request.method == "POST":
        return HttpResponseRedirect(reverse("complete_delivery"))

    # checks if the user is in the session
    if "id" in request.session:
        pass
    else:
        return HttpResponseRedirect("/auth/login/")

    # this code is executed when the seller enters with a GET request
    try:
        job_id = request.session["job_id"]
    except Exception:
        return HttpResponseRedirect(reverse("seller_orders"))

    job = Job.objects.get(pk=job_id)
    return render(request, "seller/sellerEachjobpage.html", {"job": job})


def complete_delivery(request):
    """
    Allow the seller to visit the  page via 2 methods.

    1) GET : The seller is assigned the job and the job status is updated
     and the seller can enter the otp to complete the delivery
    2) POST : The OTP entered by the seller is authenticated 
    and job is completed
    """
    # This is executed on a post request to the page

    if request.method == "POST":
        otp = request.POST.get("otp")  # retrieves the otp entered by the
        # seller
        try:
            otp = int(otp)

        except Exception:
            return HttpResponseRedirect(reverse("complete_delivery"))
        job_id = request.session["job_id"]
        job = Job.objects.get(pk=job_id)
        if job.otp is None:
            message = (
                    "Please ask the Buyer to generate to "
                     "check the order status and generate OTP"
                    )
        # job is completed if the otp is correct else he is asked again to
        # re-enter the otp
        if job.otp:
            if int(otp) == job.otp:
                print(f"job {job.otp}")
                print(f"job current status: {job}")
                job.status = "Completed"
                job.save()
                return HttpResponseRedirect(reverse("completed_jobs"))

            else:
                message = "Wrong OTP entered"
                return render(
                    request,
                    "seller/seller_finish_delivery.html",
                    {"job": job, "message": message},
                )

        return render(request, "seller/sellerEachjobpage.html", {"job": job})

    # this is executed on the get request to the page
    if "id" in request.session:
        pass
    else:
        return HttpResponseRedirect("/auth/login/")
    try:
        job_id = request.session["job_id"]
    except Exception:
        return HttpResponseRedirect(reverse("seller_orders"))
    id = request.session["id"]
    job = Job.objects.get(pk=job_id)
    current_seller = Seller.objects.get(pk=id)
    # the job is assigned to the seller and he status of the job is updated
    job.assigned_to = current_seller
    job.status = "In Progress"
    job.save()
    return render(request, "seller/seller_finish_delivery.html", {"job": job})



def completed_jobs(request):
    """
    Allow the seller to visit the  page via a GET method.

    1) GET : The seller is shown the reviews and rating and list of all the
    jobs he has completed
    """
    if "id" in request.session:
        pass
    else:
        return HttpResponseRedirect("/auth/login/")

    id = request.session["id"]
    current_user = Seller.objects.get(pk=id)
    jobs = Job.objects.filter(assigned_to=current_user, status="Completed")
    for job in jobs:
        print(job.assigned_to.id)
        print(job.status)
    return render(request, "seller/reviews.html", {"jobs": jobs})
