from django.shortcuts import render
from . import models

# Create your views here.


def home(request):
    category = models.Category.objects.all()
    return render(request,"index.html",context={
        'category':category
    })


def shop(request):
    return render(request,"shop.html")


def product_details(request):
    return render(request,"product-details.html")

def contact(request):
    return render(request,"contact.html")