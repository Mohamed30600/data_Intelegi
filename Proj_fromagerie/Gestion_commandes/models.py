from django.db import models

from Gestion_client.models import TClient
from Gestion_ligne_commande.models import TDtlcode

class TEntcde(models.Model):
    codcde = models.AutoField(primary_key=True)
    commande = models.ForeignKey(TDtlcode,blank=True, null=True,on_delete=models.SET_NULL)
    datcde = models.DateTimeField(blank=True, null=True)
    codcli = models.ForeignKey(TClient,blank=True, null=True,on_delete=models.SET_NULL)
    timbrecli = models.FloatField(blank=True, null=True)
    timbrecde = models.FloatField(blank=True, null=True)
    nbcolis = models.PositiveIntegerField(db_column='Nbcolis', blank=True, null=True)  # Field name made lowercase.
    cheqcli = models.FloatField(blank=True, null=True)
    idcondit = models.IntegerField(blank=True, null=True)
    cdecomt = models.TextField(db_column='cdeComt', blank=True, null=True)  # Field name made lowercase.
    barchive = models.IntegerField(blank=True, null=True)
    bstock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_entcde'
