from rest_framework import serializers

from Gestion_conditionnement.models import TConditionnement

class TConditionnementSerializer(serializers.ModelSerializer):
    class Meta:
        model=TConditionnement
        fields =('idcondit_id','libcondit','poidscondit','prixcond','ordreimp')
