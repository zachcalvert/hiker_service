# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('distance', models.DecimalField(default=Decimal('0.0'), max_digits=5, decimal_places=1)),
                ('difficulty', models.CharField(default=b'easy', max_length=100, verbose_name='Difficulty')),
                ('elevation_gain', models.CharField(default=b'minimal', max_length=20)),
                ('time_required', models.CharField(default=b'minimal', max_length=50)),
                ('zip_code', models.IntegerField(default=97202)),
                ('trail_type', models.CharField(max_length=30, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('city', models.CharField(max_length=30, null=True, blank=True)),
                ('peak_elevation', models.CharField(max_length=30, null=True, blank=True)),
                ('other', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
