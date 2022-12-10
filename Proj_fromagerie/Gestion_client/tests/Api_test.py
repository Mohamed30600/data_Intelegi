# from audioop import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status

# class TestListCreateClient(APITestCase):
    
#     def test_creates_client(self):
#         client={'idcom':'2','genrecli':"Mr",'nomcli':'christophe','prenomcli':'formùateur','adresse1cli':'rue diginamic','adresse2cli':'','adresse3cli':'','cpcli':'34070','villecli':'montpllier','telcli':'06','emailcli':'','portcli':'','newsletter':''},
#         response=self.client.post (reverse("listClients",client))
#         self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        
#     def test_notcreates_client(self):
#         client={'idcom':'2','genrecli':"Mr",'nomcli':'christophe','nomcli':'formùateur','adresse1cli':'rue diginamic','adresse2cli':'','adresse3cli':'','cpcli':'34070','villecli':'montpllier','telcli':'06','emailcli':'','portcli':'','newsletter':''},
#         response=self.client.post (reverse("listClients",client))
#         self.assertEqual(response.status_code,status.HTTP_201_CREATED)
#         self.assertEqual(response.data['genrecli'],'MR')
#         self.assertEqual(response.data['nomcli'],'christophe')
#         self.assertEqual(response.data['prenomcli'],'formùateur')
#         self.assertEqual(response.data['adresse1cli'],'rue diginamic')