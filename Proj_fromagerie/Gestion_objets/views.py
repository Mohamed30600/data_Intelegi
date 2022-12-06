from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView
from Gestion_objets.models import TObjet
from Gestion_objets.serializers import TObjetSerializer

class ListObjet(ListAPIView):
    queryset = TObjet.objects.all()
    serializer_class= TObjetSerializer
    
    
class CreateOnjetView (CreateAPIView):
    queryset= TObjet.objects.all()
    serializer_class=TObjetSerializer
    

class updateObjetView (UpdateAPIView):
    queryset= TObjet.objects.all()
    serializer_class=TObjetSerializer
    
class deleteObjetView (DestroyAPIView):
    queryset= TObjet.objects.all()
    serializer_class=TObjetSerializer