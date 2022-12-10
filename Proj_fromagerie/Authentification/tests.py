



from django.urls import reverse ,resolve
from django.test import SimpleTestCase, TestCase,Client


from Gestion_utilisateurs.views import ListeUtilisateurs,delUtilisateur
from Authentification.models import TUtilisateur

#test la correspondance de lurl et sa fonction
class TestUrlsUtilisateur(SimpleTestCase):
    
    def test_utilisateur_url(self):
        
        url =reverse('listeUtilisateurs')
        self.assertEquals(resolve(url).func,ListeUtilisateurs)
        
        

class TestViews(TestCase):
    
    def test_utilisateur_list_Get(self):
        
        self.client= Client()
        reponse = self.client.get(reverse('listeUtilisateurs'))
        
        self.assertEqual(reponse.status_code,200)
        self.assertTemplateUsed(reponse,'Gestion_utilisateurs/listeUtilisateurs.html')
    
