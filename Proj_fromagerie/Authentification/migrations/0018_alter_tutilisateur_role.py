# Generated by Django 4.1.3 on 2022-12-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentification', '0017_alter_tutilisateur_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutilisateur',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('OP_colis', 'OP_colis'), ('OP_stock', 'OP_stock')], default='Admin', max_length=30),
        ),
    ]
