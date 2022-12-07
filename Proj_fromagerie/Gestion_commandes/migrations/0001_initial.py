# Generated by Django 4.1.3 on 2022-12-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TEntcde',
            fields=[
                ('codcde', models.AutoField(primary_key=True, serialize=False)),
                ('datcde', models.DateTimeField(blank=True, null=True)),
                ('timbrecli', models.FloatField(blank=True, null=True)),
                ('timbrecde', models.FloatField(blank=True, null=True)),
                ('nbcolis', models.PositiveIntegerField(blank=True, db_column='Nbcolis', null=True)),
                ('cheqcli', models.FloatField(blank=True, null=True)),
                ('idcondit', models.IntegerField(blank=True, null=True)),
                ('cdecomt', models.TextField(blank=True, db_column='cdeComt', null=True)),
                ('barchive', models.IntegerField(blank=True, null=True)),
                ('bstock', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_entcde',
                'managed': False,
            },
        ),
    ]
