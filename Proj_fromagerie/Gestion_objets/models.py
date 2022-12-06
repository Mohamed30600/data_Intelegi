from django.db import models

from Gestion_conditionnement.models import TConditionnement


class TObjet(models.Model):
    codobj = models.AutoField(primary_key=True)
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

    class Meta:
        managed = True
        db_table = 't_objet'
