# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0027_auto_20180624_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='prueba',
            field=models.CharField(max_length=4, default='IPAL', choices=[('IPAL', 'IPAL'), ('IPAM', 'IPAM'), ('IPAE', 'IPAE')]),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='curso',
            field=models.CharField(max_length=20, default='INFANTIL', choices=[('INFANTIL', 'Infantil'), ('PRIMERO', 'Primero'), ('SEGUNDO', 'Segundo'), ('TERCERO', 'Tercero')]),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='curso',
            field=models.CharField(max_length=20, default='INFANTIL', choices=[('INFANTIL', 'Infantil'), ('PRIMERO', 'Primero'), ('SEGUNDO', 'Segundo'), ('TERCERO', 'Tercero')]),
        ),
    ]
