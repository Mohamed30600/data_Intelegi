from django.db import models

from Gestion_conditionnement.models import TConditionnement
from Gestion_ligne_commande.models import TDtlcode


class TObjet(models.Model):
    codobj_id = models.AutoField(primary_key=True)
    libobj = models.CharField(max_length=50, blank=True, null=True)
    tailleobj = models.CharField(db_column='Tailleobj', max_length=50, blank=True, null=True)  # Field name made lowercase.
    puobj = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    poidsobj = models.DecimalField(db_column='Poidsobj', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    indispobj = models.IntegerField(blank=True, null=True)
    o_imp = models.IntegerField(blank=True, null=True)
    o_aff = models.IntegerField(blank=True, null=True)
    o_cartp = models.IntegerField(blank=True, null=True)
    idcondit= models.ForeignKey(TConditionnement,blank=True, null=True,on_delete=models.CASCADE)
    points = models.IntegerField(blank=True, null=True)
    o_ordre_aff = models.IntegerField(blank=True, null=True)
    tDtlcode = models.ManyToManyField(TDtlcode)
    class Meta:
        managed = True
        db_table = 't_objet'
        
class TObjetDtlcode(models.Model):
    codobj = models.ForeignKey(TObjet, models.DO_NOTHING, db_column='codobj')
    commande = models.ForeignKey(TDtlcode, models.DO_NOTHING, to_field='codcde')

    class Meta:
        managed = True
        db_table = 't_objet_dtlcode'