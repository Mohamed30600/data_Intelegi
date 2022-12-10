from rest_framework import serializers

from Gestion_objets.models import TObjet


class TObjetSerializer(serializers.ModelSerializer):
    class Meta:
        model=TObjet
        fields =('codobj_id','libobj','tailleobj','puobj','poidsobj','indispobj','o_imp','o_aff','o_cartp','idcondit_id',"points","o_ordre_aff")