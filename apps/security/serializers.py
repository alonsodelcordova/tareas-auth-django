from rest_framework import serializers
from django.contrib.auth.models import User
from tareas_django.utils.base_serializers import DynamicFieldsModelSerializer

class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',  'password']
        
