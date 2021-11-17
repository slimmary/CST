from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Detail, Oil, OilContainer, Service, KitService
from .serializers import DetailSerializer, DetailBriefSerializer, OilSerializer, OilBriefSerializer,\
    OilContainerSerializer, ServiceSerializer, ServiceBriefSerializer, KitServiceSerializer, KitServiceBriefSerializer


class DetailList(generics.ListCreateAPIView):
    queryset = Detail.objects.all()
    serializer_class = DetailBriefSerializer
    pagination_class = LimitOffsetPagination


class DetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailSerializer

    def get_object(self):
        return get_object_or_404(Detail, pk=self.kwargs.get('detail_id'))


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


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceBriefSerializer
    pagination_class = LimitOffsetPagination


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer

    def get_object(self):
        return get_object_or_404(Service, pk=self.kwargs.get('service_id'))


class KitServiceList(generics.ListCreateAPIView):
    queryset = KitService.objects.all()
    serializer_class = KitServiceBriefSerializer
    pagination_class = LimitOffsetPagination


class KitServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = KitServiceSerializer

    def get_object(self):
        return get_object_or_404(KitService, pk=self.kwargs.get('kit_service_id'))

