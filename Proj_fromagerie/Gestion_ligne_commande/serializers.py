from rest_framework import serializers
from .models import TDtlcode

class TDtlcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TDtlcode
        fields =('codcde','codobj','qte','colis','commentaire')