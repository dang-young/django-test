# Generated by Django 4.2.1 on 2023-05-30 19:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(default=0)),
                ('rid', models.IntegerField(default=0)),
                ('menu', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), blank=True, size=None)),
                ('num_guest', models.IntegerField(default=0)),
                ('enter_time', models.DateTimeField(verbose_name='enter time')),
                ('out_time', models.DateTimeField(verbose_name='out time')),
                ('Total_time', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.IntegerField(default=0)),
                ('rname', models.CharField(max_length=200)),
                ('num_table', models.IntegerField(default=0)),
                ('menu0', models.CharField(max_length=20)),
                ('menu1', models.CharField(max_length=20)),
                ('menu2', models.CharField(max_length=20)),
                ('menu3', models.CharField(max_length=20)),
                ('menu4', models.CharField(max_length=20)),
                ('menu5', models.CharField(max_length=20)),
                ('menu6', models.CharField(max_length=20)),
                ('menu7', models.CharField(max_length=20)),
                ('menu8', models.CharField(max_length=20)),
            ],
        ),
    ]