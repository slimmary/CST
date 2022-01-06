from rest_framework import serializers
from .models import WorkOrder, WorkOrderItem


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = '__all__'


class WorkOrderBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = ('open_date', 'car', 'status', 'total_price', 'close_date',)


class WorkOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderItem
        fields = '__all__'
