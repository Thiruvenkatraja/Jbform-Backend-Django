# Generated by Django 4.1.5 on 2023-01-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jdform',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('candidatename', models.CharField(blank=True, max_length=50)),
                ('mobile', models.IntegerField()),
                ('technology', models.CharField(blank=True, max_length=50)),
                ('startdate', models.CharField(blank=True, max_length=50)),
                ('followupdate', models.CharField(blank=True, max_length=50)),
                ('resource', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, max_length=50)),
                ('feedback', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
