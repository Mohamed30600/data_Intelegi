# Generated by Django 4.1.3 on 2022-12-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0010_alter_tutilisateur_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutilisateur',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('OP_stock', 'OP_stock'), ('OP_colis', 'OP_colis')], default='Admin', max_length=30),
        ),
    ]
