from django.db import models
from django.contrib.auth.models import AbstractUser


class TUtilisateur(AbstractUser):
    
    
        ADMIN = 'Admin'
        OPCOLIS = 'OP_colis'
        OPSTOCK ='OP_stock'

        ROLE_CHOICES = {
            (ADMIN, 'Admin'),
            (OPCOLIS, 'OP_colis'),
            (OPSTOCK,'OP_stock'),
        }
        code_utilisateur = models.AutoField(primary_key=True)
        nom_utilisateur=models.CharField(max_length=128)
        couleur_fond_utilisateur = models.IntegerField(blank=True, null=True)
        date_cde_utilisateur = models.DateTimeField(blank=True, null=True)
        role = models.CharField(max_length=30,choices=ROLE_CHOICES,default='Admin')

        class Meta:
            managed = True