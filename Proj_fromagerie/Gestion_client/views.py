from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListAPIView ,CreateAPIView ,UpdateAPIView , DestroyAPIView

from Gestion_client.models import TClient
from Gestion_client.serializers import TClientSerializer

# appel a la serialisation pour optimer l appel a l' Apiview

#recupere la liste des client dans la basee methode get
class ListClientView(ListAPIView):
    queryset = TClient.objects.all()
    serializer_class= TClientSerializer
    
 #permet de creer un client dans la base methode post   
class CreateClientView (CreateAPIView):
    queryset= TClient.objects.all()
    serializer_class=TClientSerializer
    
#mise a jour d'un client dans la base methode put
class updateClientView (UpdateAPIView):
    queryset= TClient.objects.all()
    serializer_class=TClientSerializer
#suppression dun client dans la base methode delete    
class deleteClientView (DestroyAPIView):
    queryset= TClient.objects.all()
    serializer_class=TClientSerializer

#authentification a mettre en place pour differencier les perimetre métier
#   authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]