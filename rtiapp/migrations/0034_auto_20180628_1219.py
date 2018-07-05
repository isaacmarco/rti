# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0033_evaluador_curso_academico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion_ipae_primero',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_segundo',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_tercero',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_infantil',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_primero',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_infantil',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_primero',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_segundo',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_tercero',
            name='observaciones',
        ),
    ]
