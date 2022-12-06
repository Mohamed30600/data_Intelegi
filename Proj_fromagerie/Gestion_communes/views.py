from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_communes.models import TCommunes
from Gestion_communes.serializers import TCommuneSerializer

class ListcommuneView(ListAPIView):
    queryset = TCommunes.objects.all()
    serializer_class= TCommuneSerializer
    
    
class CreateCommuneView (CreateAPIView):
    queryset= TCommunes.objects.all()
    serializer_class=TCommuneSerializer
    

class updateCommuneView (UpdateAPIView):
    queryset= TCommunes.objects.all()
    serializer_class=TCommuneSerializer
    
class deleteCommuneView (DestroyAPIView):
    queryset= TCommunes.objects.all()
    serializer_class=TCommuneSerializer