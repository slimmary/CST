from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import WorkOrder, WorOrderItem
from .serializers import WorkOrderSerializer, WorkOrderBriefSerializer, WorOrderItemSerializer


class WorkOrderList(generics.ListCreateAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderBriefSerializer
    pagination_class = LimitOffsetPagination


class WorkOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderSerializer

    def get_object(self):
        return get_object_or_404(WorkOrder, pk=self.kwargs.get('work_order_id'))


class WorOrderItemList(generics.ListCreateAPIView):
    queryset = WorOrderItem.objects.all()
    serializer_class = WorOrderItemSerializer
    pagination_class = LimitOffsetPagination


class WorOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorOrderItemSerializer

    def get_object(self):
        return get_object_or_404(WorOrderItem, pk=self.kwargs.get('work_order_item_id'))
