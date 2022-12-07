from rest_framework import serializers
from .models import TClient

class TClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=TClient
        fields =('codcli_id','genrecli','nomcli','prenomcli','adresse1cli','adresse2cli','adresse3cli','cpcli','villecli','telcli','emailcli','portcli','newsletter')