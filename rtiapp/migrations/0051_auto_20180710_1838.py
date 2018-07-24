# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0050_auto_20180709_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='momento',
            field=models.CharField(max_length=10, default='PROGRESO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
    ]
