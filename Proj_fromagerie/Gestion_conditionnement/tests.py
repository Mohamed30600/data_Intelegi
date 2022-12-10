import unittest

from Gestion_conditionnement.models import TConditionnement

class testConditionement(unittest.TestCase):
    

        
     #tester le modele commune   
    def setUp(self):
           TConditionnement.objects.create (
            libcondit="enveloppe",
            poidscondit=5,
            prixcond=0.0001,
            ordreimp=2
                )
        
    def test_condi_is_created(self):
       libelle1 =TConditionnement.objects.get(libcondit="enveloppe")
       self.assertEqual(libelle1.libcondit,"enveloppe")