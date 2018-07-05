# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0025_auto_20180624_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='mes_leible',
            field=models.CharField(max_length=10, default='noviembre'),
        ),
    ]
