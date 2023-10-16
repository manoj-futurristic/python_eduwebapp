from edu_auth.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import *
from rest_framework import status
from .serializers import *
import json


# Create your views here.

class CategoryApi(APIView):
    @staticmethod
    def get(request): 
        try: 
            query = request.GET.get('category_id')
            print(query)
            if(query):
                category = Category.objects.get(pk=query)
                serializer = category_Serializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)

            cobj = Category.objects.all()
            print(cobj)
            categoryobj = category_Serializer(cobj,many=True).data
            return Response({'status':True,'message':'categories get successfully','categories': categoryobj}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"status":False,'message':"categories not found",}, status=status.HTTP_404_NOT_FOUND)