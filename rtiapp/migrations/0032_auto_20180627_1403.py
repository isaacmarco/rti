# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0031_auto_20180626_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAE_FIN',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAE_INICIO',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAE_MEDIO',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAL_FIN',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAL_INICIO',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAL_MEDIO',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAM_FIN',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAM_INICIO',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='alumno',
            name='riesgo_IPAM_MEDIO',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('ALTR', 'Alto riesgo'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='ADIVINANZAS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
