"""
Here we need to create model serializers because the response object could not handle 
complex datatype such as Django model instances. So before rendering we need to serialize the data.
"""
from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # fields that we want to serialize