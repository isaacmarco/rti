# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0010_auto_20180622_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
    ]
