from django.db import models

from Gestion_communes.models import TCommunes

class TClient(models.Model):
    codcli_id = models.AutoField(primary_key=True)
    idcom=models.ForeignKey(TCommunes,blank=True, null=True,on_delete=models.SET_NULL)
    genrecli = models.CharField(max_length=8, blank=True, null=True)
    nomcli = models.CharField(max_length=40)
    prenomcli = models.CharField(max_length=30, blank=True, null=True)
    adresse1cli = models.CharField(max_length=50, blank=True, null=True)
    adresse2cli = models.CharField(max_length=50, blank=True, null=True)
    adresse3cli = models.CharField(max_length=255, blank=True, null=True)
    cpcli = models.CharField(max_length=5, blank=True, null=True)
    villecli = models.CharField(max_length=50, blank=True, null=True)
    telcli = models.CharField(max_length=10, blank=True, null=True)
    emailcli = models.TextField(blank=True, null=True)
    portcli = models.CharField(max_length=10, blank=True, null=True)
    newsletter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_client'