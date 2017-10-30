# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-26 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/', verbose_name='')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='')),
            ],
        ),
    ]