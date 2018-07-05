# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0036_auto_20180703_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='DICTADO_FRASES',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(21), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='DICTADO_ORTOGRAFIA_ARBITRARIA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='DICTADO_ORTOGRAFIA_REGLADA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='DICTADO_PSEUDOPALABRAS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='TLC_1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(108), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='DICTADO_FRASES',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(21), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='DICTADO_ORTOGRAFIA_ARBITRARIA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='DICTADO_ORTOGRAFIA_REGLADA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='DICTADO_PSEUDOPALABRAS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='TLC_1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(108), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='DICTADO_FRASES',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(21), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='DICTADO_ORTOGRAFIA_ARBITRARIA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='DICTADO_ORTOGRAFIA_REGLADA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='PDC_5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(77), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='SEC_5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='SEC_SEI_5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='ADIVINANZAS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='CFA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(80), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='CLE_IMAGEN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(35), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='CLE_TEXTO',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='CNL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='CSL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='CFS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(85), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='CLE_TEXTO',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='CNL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='CSL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='FLO',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(133), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='LP',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='TM',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='CFS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='CLE_TEXTO',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='CNL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='CSL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='FLO',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(133), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='LP',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='PRO',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='TM',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='VOC',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='CM',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='CN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='CVA',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='EC',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(36), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='IN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(63), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='SN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(36), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='CN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='ODD',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='OUD',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='SN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='VP',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='CN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='ODD',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='OUD',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='SN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='VP',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='CN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='ODD',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='OUD',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='SN',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='VP',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(45), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='latitud',
            field=models.DecimalField(default=0, max_digits=14, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='longitud',
            field=models.DecimalField(default=0, max_digits=14, decimal_places=10),
        ),
    ]
