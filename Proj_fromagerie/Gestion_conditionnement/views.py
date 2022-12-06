from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_conditionnement.models import TConditionnement
from Gestion_conditionnement.serializers import TConditionnementSerializer

class ListConditionnementView(ListAPIView):
    queryset = TConditionnement.objects.all()
    serializer_class= TConditionnementSerializer
    
    
class CreateConditionnementView (CreateAPIView):
    queryset= TConditionnement.objects.all()
    serializer_class=TConditionnementSerializer
    

class updateConditionnementView (UpdateAPIView):
    queryset= TConditionnement.objects.all()
    serializer_class=TConditionnementSerializer
    
class deleteConditionnementView (DestroyAPIView):
    queryset= TConditionnement.objects.all()
    serializer_class=TConditionnementSerializer