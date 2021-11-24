from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Part, Oil, OilContainer, Work, KitService
from .serializers import PartSerializer, PartBriefSerializer, OilSerializer, OilBriefSerializer,\
    OilContainerSerializer, WorkSerializer, KitServiceSerializer, KitServiceBriefSerializer


class PartList(generics.ListCreateAPIView):
    queryset = Part.objects.all()
    serializer_class = PartBriefSerializer
    pagination_class = LimitOffsetPagination


class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PartSerializer

    def get_object(self):
        return get_object_or_404(Part, pk=self.kwargs.get('detail_id'))


class OilList(generics.ListCreateAPIView):
    queryset = Oil.objects.all()
    serializer_class = OilBriefSerializer
    pagination_class = LimitOffsetPagination


class OilDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OilSerializer

    def get_object(self):
        return get_object_or_404(Oil, pk=self.kwargs.get('oil_id'))


class OilContainerList(generics.ListCreateAPIView):
    queryset = OilContainer.objects.all()
    serializer_class = OilContainerSerializer
    pagination_class = LimitOffsetPagination


class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    pagination_class = LimitOffsetPagination


class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkSerializer

    def get_object(self):
        return get_object_or_404(Work, pk=self.kwargs.get('work_id'))


class KitServiceList(generics.ListCreateAPIView):
    queryset = KitService.objects.all()
    serializer_class = KitServiceBriefSerializer
    pagination_class = LimitOffsetPagination


class KitServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KitServiceSerializer

    def get_object(self):
        return get_object_or_404(KitService, pk=self.kwargs.get('kit_service_id'))

