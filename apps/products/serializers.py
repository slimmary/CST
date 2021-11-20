from rest_framework import serializers
from .models import Part, Oil, Work, KitService, OilContainer


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class PartBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('product_name', 'part_number_original', 'part_manufacturer', 'part_number_cross', 'is_available')


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


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class WorkBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('service_name', 'work_our')


class KitServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitService
        fields = '__all__'


class KitServiceBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitService
        fields = ('service_name', 'work_our')