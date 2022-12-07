from rest_framework import serializers

from Gestion_poids.models import TPoids
from Gestion_poids.models import TPoidsv


class TPoidSerializer(serializers.ModelSerializer):
    class Meta:
        model=TPoids
        fields =('valmin','valtimbre')
        

class TPoidvSerializer(serializers.ModelSerializer):
    class Meta:
        model=TPoidsv
        fields =('valmin','valtimbre')