from rest_framework import serializers
from .models import ClientProfile


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'


class ClientProfileBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ('phone',)
