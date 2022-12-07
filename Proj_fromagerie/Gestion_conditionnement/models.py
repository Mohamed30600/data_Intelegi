from django.db import models

class TConditionnement(models.Model):
    idcondit_id = models.IntegerField(primary_key=True)
    libcondit = models.CharField(max_length=50, blank=True, null=True)
    poidscondit = models.IntegerField(blank=True, null=True)
    prixcond = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ordreimp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_conditionnement'
