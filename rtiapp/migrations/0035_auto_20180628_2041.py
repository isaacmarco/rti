# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0034_auto_20180628_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='ultima_evaluacion_curso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alumno',
            name='ultima_evaluacion_mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
    ]
