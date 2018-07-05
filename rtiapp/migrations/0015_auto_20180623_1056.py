# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0014_auto_20180623_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion_ipae_primero',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_segundo',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_tercero',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_infantil',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_primero',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_infantil',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_primero',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_segundo',
            name='id_alumno',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_tercero',
            name='id_alumno',
        ),
    ]
