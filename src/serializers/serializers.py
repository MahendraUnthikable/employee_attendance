from rest_framework import serializers
from ..models.models import employeeRegistratoin

class registratoinSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(required=False,max_length=100)
    last_name=serializers.CharField(required=False,max_length=100)
    email=serializers.CharField(required=True,max_length=100)
    password=serializers.CharField(required=True,max_length=100)
    phone=serializers.CharField(required=False,max_length=100)

    class Meta:
        model = employeeRegistratoin
        fields = ('__all__')

             