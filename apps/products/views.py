from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Part, Oil, OilContainer, Work, KitService
from .serializers import PartSerializer, PartBriefSerializer, OilSerializer, OilBriefSerializer, \
    OilContainerSerializer, WorkSerializer, KitServiceSerializer, KitServiceBriefSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnlyMethod


class PartList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]
    serializer_class = PartBriefSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return Part.objects.all()
        return Part.objects.filter(work_order_item_part__work_order__car__client__user=self.request.user)


class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PartSerializer
        return PartBriefSerializer

    def get_object(self):
        if self.request.user.is_staff:
            return get_object_or_404(Part, pk=self.kwargs.get('part_id'))
        return get_object_or_404(Part, pk=self.kwargs.get('part_id'),
                                 work_order_item_part__work_order__car__client__user=self.request.user)


class OilList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return OilSerializer
        return OilBriefSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Oil.objects.all()
        return Oil.objects.filter(work_order_item_oil__work_order__car__client__user=self.request.user)


class OilDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return OilSerializer
        return OilBriefSerializer

    def get_object(self):
        if self.request.user.is_staff:
            return get_object_or_404(Oil, pk=self.kwargs.get('oil_id'), )
        return get_object_or_404(Oil, pk=self.kwargs.get('oil_id'),
                                 work_order_item_oil__work_order__car__client__user=self.request.user)


class OilContainerList(generics.ListCreateAPIView):
    queryset = OilContainer.objects.all()
    serializer_class = OilContainerSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = IsAdminUser


class WorkList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]
    serializer_class = WorkSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return Work.objects.all()
        return Work.objects.filter(work_order_item_service__work_order__car__client__user=self.request.user)


class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]
    serializer_class = WorkSerializer

    def get_object(self):
        if self.request.user.is_staff:
            return get_object_or_404(Work, pk=self.kwargs.get('work_id'))
        return get_object_or_404(Work, pk=self.kwargs.get('work_id'),
                                 work_order_item_service__work_order__car__client__user=self.request.user)


class KitServiceList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]
    serializer_class = KitServiceBriefSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        if self.request.user.is_staff:
            return KitService.objects.all()
        return KitService.objects.filter(work_order_item_kit_service__work_order__car__client__user=self.request.user)


class KitServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated & (IsAdminUser | ReadOnlyMethod)]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return KitServiceSerializer
        return KitServiceBriefSerializer

    def get_object(self):
        return get_object_or_404(KitService, pk=self.kwargs.get('kit_service_id'),
                                 work_order_item_kit_service__work_order__car__client__user=self.request.user)
