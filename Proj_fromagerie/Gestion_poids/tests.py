from django.test import TestCase
from Gestion_poids.models import TPoids
from django.urls import reverse


class Update_models_tests(TestCase):
    def setUp(self):
        TPoids.objects.create(valmin=18000, valtimbre=10)

    def test_objet(self):
        objet_temp = TPoids.objects.latest('valmin')
        valmin = objet_temp.valmin
        url = reverse('Gestion_poids:modif', args=[valmin])
        reponse = self.client.get(url)
        assert reponse.status_code == 200