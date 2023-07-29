from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about_us(request):
    return render(request, "main/aboutus.html")

def get_started(request):
    return render(request, "main/get_started.html")

def buyer_or_seller(request):
    return render(request, "main/buyerorseller.html")
