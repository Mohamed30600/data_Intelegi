from rest_framework import serializers
from .models import TEntcde

class TEntcdeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TEntcde
        fields =('codcde','datcde','codcli','timbrecli','nbcolis','cheqcli','idcondit','cdecomt','barchive','bstock')