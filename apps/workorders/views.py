from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import ReadOnlyMethod
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import WorkOrder, WorkOrderItem
from .serializers import WorkOrderSerializer, WorkOrderBriefSerializer, WorkOrderItemSerializer


class WorkOrderList(generics.ListCreateAPIView):
    serializer_class = WorkOrderBriefSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]

    def get_queryset(self):
        if self.request.user.is_staff:
            return WorkOrder.objects.all()
        else:
            return WorkOrder.objects.filter(car__client__user=self.request.user)


class WorkOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return WorkOrderSerializer
        return WorkOrderBriefSerializer

    def get_object(self):
        if self.request.user.is_staff:
            return get_object_or_404(WorkOrder, pk=self.kwargs.get('work_order_id'))
        else:
            return get_object_or_404(WorkOrder, pk=self.kwargs.get('work_order_id'), car__client__user=self.request.user)


class WorkOrderItemList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]
    serializer_class = WorkOrderItemSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return WorkOrderItem.objects.all()
        else:
            return WorkOrderItem.objects.filter(work_order__car__client__user=self.request.user)


class WorkOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOrderItemSerializer
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]

    def get_object(self):
        if self.request.user.is_staff:
            return get_object_or_404(WorkOrderItem, pk=self.kwargs.get('work_order_item_id'))
        else:
            return get_object_or_404(WorkOrderItem, pk=self.kwargs.get('work_order_item_id'),
                                     work_order__car__client__user=self.request.user)
