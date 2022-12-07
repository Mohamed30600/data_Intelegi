from django.shortcuts import render

from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_ligne_commande.serializers import TDtlcodeSerializer

from .models import TDtlcode

class ListDtlcodeView(ListAPIView):
    queryset = TDtlcode.objects.all()
    serializer_class= TDtlcodeSerializer
    
    
class CreateDtlcodeView (CreateAPIView):
    queryset= TDtlcode.objects.all()
    serializer_class=TDtlcodeSerializer
    

class updateDtlcodeView (UpdateAPIView):
    queryset= TDtlcode.objects.all()
    serializer_class=TDtlcodeSerializer
    
class deleteDtlcodeView (DestroyAPIView):
    queryset= TDtlcode.objects.all()
    serializer_class=TDtlcodeSerializer