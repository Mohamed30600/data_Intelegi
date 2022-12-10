# Generated by Django 4.1.3 on 2022-12-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TObjet',
            fields=[
                ('codobj', models.IntegerField(primary_key=True, serialize=False)),
                ('libobj', models.CharField(blank=True, max_length=50, null=True)),
                ('tailleobj', models.CharField(blank=True, db_column='Tailleobj', max_length=50, null=True)),
                ('puobj', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True)),
                ('poidsobj', models.DecimalField(blank=True, db_column='Poidsobj', decimal_places=4, max_digits=19, null=True)),
                ('indispobj', models.IntegerField(blank=True, null=True)),
                ('o_imp', models.IntegerField(blank=True, null=True)),
                ('o_aff', models.IntegerField(blank=True, null=True)),
                ('o_cartp', models.IntegerField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, null=True)),
                ('o_ordre_aff', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_objet',
                'managed': True,
            },
        ),
    ]
