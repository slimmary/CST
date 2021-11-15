from rest_framework import serializers
from .models import Car, BrandModel


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('brand_model', 'year_manufacturing', 'car_number')
