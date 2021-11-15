from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Car, BrandModel
from .serializers import BrandModelSerializer, CarSerializer, CarBriefSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarBriefSerializer
    pagination_class = LimitOffsetPagination


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer

    def get_object(self):
        return get_object_or_404(Car, pk=self.kwargs.get('car_id'))


class BrandModelList(generics.ListCreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandModelSerializer
    pagination_class = LimitOffsetPagination


class BrandModelDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BrandModelSerializer

    def get_object(self):
        return get_object_or_404(BrandModel, pk=self.kwargs.get('brand_model_id'))

