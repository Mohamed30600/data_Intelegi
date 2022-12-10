import unittest
from django.test import Client
from django.urls import reverse
from Gestion_communes.forms import CommuneForm
from Gestion_communes.models import TCommunes

class testCommune(unittest.TestCase):
    
    def test_formulaire_create_commune(self):
        form=CommuneForm (data={"dep":"2","cp":"34400","ville":"lunel"})
        self.assertTrue(form.is_valid())
        
     #tester le modele commune   
    def setUp(self):
          self.commune = TCommunes.objects.create (
                dep=1,
                cp='34250',
                communes="vendargue",
                )
          self.client = Client()
        
    def test_commune_is_created(self):
       commune1 =TCommunes.objects.get(communes="vendargue")
       self.assertEqual(commune1.communes,'vendargue')


    

    def test_commune_successful_delete(self):
                payload ={
                        'dep':1,
                        'cp':'34250',
                        'communes':"vendargue",
                }
                TCommunes.objects.create(**payload)
                commune = TCommunes.objects.get()
                response = self.client.delete(reverse('commune'))