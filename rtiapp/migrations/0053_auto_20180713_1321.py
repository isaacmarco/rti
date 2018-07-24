# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0052_auto_20180710_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='evaluado',
            field=models.BooleanField(default=False),
        ),
    ]
