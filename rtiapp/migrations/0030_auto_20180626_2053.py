# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0029_auto_20180626_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='centro',
            field=models.CharField(max_length=100, default='Centro'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='riesgo_IPAE',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='riesgo_IPAL',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='riesgo_IPAM',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
    ]
