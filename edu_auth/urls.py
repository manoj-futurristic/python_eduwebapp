from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("product_details/", views.product_details, name="product_details"),
    path("contact/", views.contact, name="contact"),
]
