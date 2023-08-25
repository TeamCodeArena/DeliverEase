"""This module contains views of main app"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "main/index.html")


def about_us(request):
    return render(request, "main/aboutus.html")


def get_started(request):
    return render(request, "main/get_started.html")


def red_home(request):
    if "buyer_id" in request.session:
        return HttpResponseRedirect(reverse("index"))
    elif "id" in request.session:
        return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("login"))


def buyer_or_seller(request):
    return render(request, "main/buyerorseller.html")
