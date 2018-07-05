# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0008_alumno_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='pais',
            field=models.CharField(max_length=2, default='ESP', choices=[('ESP', 'España'), ('GTM', 'Guatemala'), ('ECU', 'Ecuador'), ('CAN', 'Canarias')]),
        ),
    ]
