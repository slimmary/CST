from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrAdmin, ReadOnlyMethod
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import WorkOrder, WorOrderItem
from .serializers import WorkOrderSerializer, WorkOrderBriefSerializer, WorOrderItemSerializer


class WorkOrderList(generics.ListCreateAPIView):
    serializer_class = WorkOrderBriefSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [ReadOnlyMethod, IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return WorkOrder.objects.all()
        if self.request.user.profile:
            return WorkOrder.objects.filter(car__client=self.request.user.profile)


class WorkOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return WorkOrderSerializer
        return WorkOrderBriefSerializer

    def get_object(self):
        return get_object_or_404(WorkOrder, pk=self.kwargs.get('work_order_id'))


class WorOrderItemList(generics.ListCreateAPIView):
    queryset = WorOrderItem.objects.all()
    serializer_class = WorOrderItemSerializer
    pagination_class = LimitOffsetPagination


class WorOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorOrderItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self):
        return get_object_or_404(WorOrderItem, pk=self.kwargs.get('work_order_item_id'))
