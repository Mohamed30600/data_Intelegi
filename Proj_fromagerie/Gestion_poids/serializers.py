from rest_framework import serializers

from Gestion_objets.models import TObjet


class TPoid(serializers.ModelSerializer):
    class Meta:
        model=TObjet
        fields =('valmin','valtimbre')
        

class TPoidv(serializers.ModelSerializer):
    class Meta:
        model=TObjet
        fields =('valmin','valtimbre')