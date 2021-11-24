from rest_framework import serializers
from .models import WorkOrder, WorOrderItem


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class WorkOrderBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ('open_date', 'car', 'status', 'av_price', 'total_price', 'close_date',)


class WorOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorOrderItem
        fields = '__all__'
