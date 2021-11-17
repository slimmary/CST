from rest_framework import serializers
from .models import Detail, Oil, Service, KitService, OilContainer


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = '__all__'


class DetailBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ('product_name', 'detail_number_original', 'detail_manufacturer', 'detail_number_cross', 'is_available')


class OilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oil
        fields = '__all__'


class OilBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oil
        fields = ('product_name', 'stock_l', 'is_available')


class OilContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OilContainer
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('product_name', 'work_our')


class KitServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitService
        fields = '__all__'


class KitServiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitService
        fields = ('product_name', 'kit_work_ours')