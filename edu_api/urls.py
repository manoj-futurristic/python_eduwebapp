from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
   path('getCategory/',CategoryApi.as_view(),name='getCategory'),
]