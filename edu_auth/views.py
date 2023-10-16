from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"index.html")


def shop(request):
    return render(request,"shop.html")


def product_details(request):
    return render(request,"product-details.html")

def contact(request):
    return render(request,"contact.html")