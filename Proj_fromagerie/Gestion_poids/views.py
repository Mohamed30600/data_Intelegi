from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_poids.models import TPoids
from data_Intelegi.Proj_fromagerie.Gestion_objets.serializers import TObjetSerializer
from data_Intelegi.Proj_fromagerie.Gestion_poids.serializers import TPoidv

class ListPoid(ListAPIView):
    queryset = TPoids.objects.all()
    serializer_class= TObjetSerializer
    
    
class CreatePoidView (CreateAPIView):
    queryset= TPoids.objects.all()
    serializer_class=TObjetSerializer
    

class updatePoidView (UpdateAPIView):
    queryset= TPoids.objects.all()
    serializer_class=TObjetSerializer
    
class deletePoidView (DestroyAPIView):
    queryset= TPoids.objects.all()
    serializer_class=TObjetSerializer
    
    
    
class ListPoidv(ListAPIView):
    queryset = TPoidv.objects.all()
    serializer_class= TObjetSerializer
    
    
class CreatePoidvView (CreateAPIView):
    queryset= TPoidv.objects.all()
    serializer_class=TObjetSerializer
    

class updatePoidvView (UpdateAPIView):
    queryset= TPoidv.objects.all()
    serializer_class=TObjetSerializer
    
class deletePoidvView (DestroyAPIView):
    queryset= TPoidv.objects.all()
    serializer_class=TObjetSerializer