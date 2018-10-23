# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0054_evaluador_centro_pilotaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='centro_pilotaje',
            field=models.CharField(max_length=50, default='Centro pilotaje'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='codigo_evaluador',
            field=models.CharField(max_length=20, default='Codigo'),
        ),
        migrations.AddField(
            model_name='evaluador',
            name='codigo',
            field=models.CharField(max_length=20, default='Codigo'),
        ),
    ]
