# Generated by Django 4.1.3 on 2022-12-04 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_conditionnement', '0002_remove_tconditionnement_id_and_more'),
        ('Gestion_objets', '0005_remove_tobjet_id_alter_tobjet_codobj_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tobjet',
            options={'default_related_name': 't_objet'},
        ),
        migrations.AlterField(
            model_name='tobjet',
            name='idcondit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestion_conditionnement.tconditionnement'),
        ),
        migrations.AlterModelTable(
            name='tobjet',
            table=None,
        ),
    ]
