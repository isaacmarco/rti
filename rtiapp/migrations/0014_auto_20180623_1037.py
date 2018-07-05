# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0013_auto_20180623_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='mes',
            field=models.CharField(max_length=20, default='NOVIEMBRE', choices=[('NOVIEMBRE', 'Noviembre'), ('DICIEMBRE', 'Diciembre'), ('ENERO', 'Enero'), ('FEBRERO', 'Febrero'), ('MARZO', 'Marzo'), ('ABRIL', 'Abril'), ('MAYO', 'Mayo'), ('JUNIO', 'Junio')]),
        ),
    ]
