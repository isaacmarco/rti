# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0026_auto_20180624_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='observaciones',
            field=models.TextField(default='Sin observaciones'),
        ),
    ]
