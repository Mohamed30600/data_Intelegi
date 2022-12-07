from django.db import models



class TDtlcode(models.Model):
    commande_id = models.AutoField(primary_key=True)
    codcde = models.IntegerField(blank=True, null=True)
    codobj = models.IntegerField( blank=True, null=True)
    qte = models.IntegerField(blank=True, null=True)
    colis = models.IntegerField(db_column='Colis', blank=True, null=True)  # Field name made lowercase.
    commentaire = models.CharField(db_column='Commentaire', max_length=100, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = True
        db_table = 't_dtlcode'