from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from .models import TUtilisateur
from Gestion_communes.serializers import TCommuneSerializer

class ListUtilisateurView(ListAPIView):
    queryset = TUtilisateur.objects.all()
    serializer_class= TCommuneSerializer
    
    
class CreateutilisateurView (CreateAPIView):
    queryset= TUtilisateur.objects.all()
    serializer_class=TCommuneSerializer
    

class updateUtilisateurView (UpdateAPIView):
    queryset= TUtilisateur.objects.all()
    serializer_class=TCommuneSerializer
    
class deleteUtilisateurView (DestroyAPIView):
    queryset= TUtilisateur.objects.all()
    serializer_class=TCommuneSerializer

