from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_commandes.serializers import TEntcdeSerializer

from .models import TEntcde

class ListEntcdeView(ListAPIView):
    queryset = TEntcde.objects.all()
    serializer_class= TEntcdeSerializer
    
    
class CreateEntcdeView (CreateAPIView):
    queryset= TEntcde.objects.all()
    serializer_class=TEntcdeSerializer
    

class updateEntdeView (UpdateAPIView):
    queryset= TEntcde.objects.all()
    serializer_class=TEntcdeSerializer
    
class deleteEntdeView (DestroyAPIView):
    queryset= TEntcde.objects.all()
    serializer_class=TEntcdeSerializer
