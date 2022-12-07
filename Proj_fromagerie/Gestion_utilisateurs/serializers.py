from rest_framework import serializers
from .models import TUtilisateur

class TUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model=TUtilisateur
        fields =('code_utilisateur','nom_utilisateur','prenom_utilisateur','couleurd_fond_utilisateur','date_cde_utilisateur')