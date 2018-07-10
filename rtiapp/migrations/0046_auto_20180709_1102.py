# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0045_alumno_cial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='CIAL',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='nombre',
        ),
        migrations.AddField(
            model_name='alumno',
            name='codigo',
            field=models.CharField(max_length=100, default='código del alumno'),
        ),
    ]
