# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0020_evaluador_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='grupo',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
    ]
