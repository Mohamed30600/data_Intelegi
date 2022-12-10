from django.test import TestCase

from audioop import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class TestListCreateCommune(APITestCase):
    
    # def test_creates_comune(self):
    #     client={'dep':"2",'cp':'34250','communes':'lunel'},
    #     response=self.client.post (reverse("listCommune",client))
    #     self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
        
    def test_notcreates_comune(self):
        commune={'dep':"2",'cp':'34250','communes':'lunel'},
        
        response=self.client.post (reverse("listCommune",commune))
        #self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(response.data['dep'],'2')
        self.assertEqual(response.data['cp'],'34250')
        self.assertEqual(response.data['communes'],'lunel')