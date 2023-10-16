from edu_auth.models import *
from rest_framework import serializers


class category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'