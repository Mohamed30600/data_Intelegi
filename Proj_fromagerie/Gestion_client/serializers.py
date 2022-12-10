from rest_framework import serializers
from .models import TClient
#serialisation pour optimiser l appel a l'api avec les attribur le classe Tclient
class TClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=TClient
        fields =('codcli_id','idcom','genrecli','nomcli','prenomcli','adresse1cli','adresse2cli','adresse3cli','cpcli','villecli','telcli','emailcli','portcli','newsletter','idcom_id')