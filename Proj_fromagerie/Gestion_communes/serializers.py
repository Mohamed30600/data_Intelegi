from rest_framework import serializers
from .models import TCommunes

class TCommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model=TCommunes
        fields =('idcom','dep','cp','communes')