from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 
                  'name', 
                  'address', 
                  'price',
                  'latitude', 
                  'longitude', 
                ]