from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import ClientProfile
from .serializers import ClientProfileSerializer, ClientProfileBriefSerializer


class ClientProfileList(generics.ListCreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileBriefSerializer
    pagination_class = LimitOffsetPagination


class ClientProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientProfileSerializer

    def get_object(self):
        return get_object_or_404(ClientProfile, pk=self.kwargs.get('client_profile_id'))
