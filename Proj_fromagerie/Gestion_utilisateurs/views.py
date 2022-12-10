from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from data_Intelegi.Proj_fromagerie.Gestion_utilisateurs.serializers import TUtilisateurSerializer

from .models import TUtilisateur

class ListUtilisateurView(ListAPIView):
    queryset = TUtilisateur.objects.all()
    serializer_class= TUtilisateurSerializer
    
    
class CreateutilisateurView (CreateAPIView):
    queryset= TUtilisateur.objects.all()
    serializer_class=TUtilisateurSerializer
    

class updateUtilisateurView (UpdateAPIView):
    queryset= TUtilisateur.objects.all()
    serializer_class=TUtilisateurSerializer
    
class deleteUtilisateurView (DestroyAPIView):
    queryset= TUtilisateur.objects.all()
    serializer_class=TUtilisateurSerializer

