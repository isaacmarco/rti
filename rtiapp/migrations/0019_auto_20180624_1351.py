# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0018_auto_20180624_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion_ipae_primero',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_segundo',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_tercero',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_primero',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_infantil',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_primero',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_segundo',
            name='GLOBAL',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_tercero',
            name='GLOBAL',
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAE',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAL',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAM',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
    ]
