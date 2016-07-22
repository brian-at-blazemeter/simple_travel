# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('name', models.CharField(max_length=128, verbose_name='airline name')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('name', models.CharField(max_length=128, verbose_name='flight name')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('flight_number', models.IntegerField(verbose_name='flight number')),
                ('depart', models.DateTimeField(verbose_name='departure time')),
                ('arrive', models.DateTimeField(verbose_name='arrival time')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='price')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('address', models.CharField(max_length=128, verbose_name='address')),
                ('city', models.CharField(max_length=128, verbose_name='city')),
                ('state', models.CharField(max_length=2, verbose_name='state')),
                ('zip_code', models.IntegerField(verbose_name='zip code')),
                ('card_type', models.CharField(choices=[('VISA', 'VISA'), ('MC', 'MasterCard')], default='VISA', max_length=16, verbose_name='card type')),
                ('card_number', models.IntegerField(verbose_name='card number')),
                ('name_on_card', models.CharField(max_length=128, verbose_name='name on card')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(verbose_name='timestamp')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.City')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_route', to='flights.City')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.Route'),
        ),
    ]