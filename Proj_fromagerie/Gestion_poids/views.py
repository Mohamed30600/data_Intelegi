from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_poids.models import TPoids ,TPoidsv

from Gestion_poids.serializers import TPoidSerializer,TPoidvSerializer

class ListPoid(ListAPIView):
    queryset = TPoids.objects.all()
    serializer_class= TPoidSerializer
    
    
class CreatePoidView (CreateAPIView):
    queryset= TPoids.objects.all()
    serializer_class=TPoidSerializer
    

class updatePoidView (UpdateAPIView):
    queryset= TPoids.objects.all()
    serializer_class=TPoidSerializer
    
class deletePoidView (DestroyAPIView):
    queryset= TPoids.objects.all()
    serializer_class=TPoidSerializer
    
    
    
class ListPoidv(ListAPIView):
    queryset = TPoidsv.objects.all()
    serializer_class= TPoidvSerializer
    
    
class CreatePoidvView (CreateAPIView):
    queryset= TPoidsv.objects.all()
    serializer_class=TPoidvSerializer
    

class updatePoidvView (UpdateAPIView):
    queryset= TPoidsv.objects.all()
    serializer_class=TPoidvSerializer
    
class deletePoidvView (DestroyAPIView):
    queryset= TPoidsv.objects.all()
    serializer_class=TPoidvSerializer