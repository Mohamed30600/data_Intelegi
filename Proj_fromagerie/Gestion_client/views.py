from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_client.models import TClient
from Gestion_client.serializers import TClientSerializer



class ListClientView(ListAPIView):
    queryset = TClient.objects.all()
    serializer_class= TClientSerializer
    
    
class CreateClientView (CreateAPIView):
    queryset= TClient.objects.all()
    serializer_class=TClientSerializer
    

class updateClientView (UpdateAPIView):
    queryset= TClient.objects.all()
    serializer_class=TClientSerializer
    
class deleteClientView (DestroyAPIView):
    queryset= TClient.objects.all()
    serializer_class=TClientSerializer
