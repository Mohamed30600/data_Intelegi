from django.db import models

class TCommunes(models.Model):
    idcom_id = models.AutoField(primary_key=True)
    dep = models.PositiveIntegerField(db_column='DEP', blank=True, null=True)  # Field name made lowercase.
    cp = models.CharField(db_column='CP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    communes = models.CharField(db_column='COMMUNES', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 't_communes'
