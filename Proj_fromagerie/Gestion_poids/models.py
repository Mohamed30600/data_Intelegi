from django.db import models

class TPoids(models.Model):
    valmin = models.FloatField(primary_key=True)
    valtimbre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_poids'


class TPoidsv(models.Model):
    valmin = models.FloatField(primary_key=True)
    valtimbre = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_poidsv'
# Create your models here.
