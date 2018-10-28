# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0058_auto_20181027_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='isla',
            field=models.CharField(max_length=20, default='NINGUNA', choices=[('NINGUNA', 'Ninguna'), ('TENERIFE', 'Tenerife'), ('GOMERA', 'Gomera'), ('PALMA', 'Palma'), ('HIERRO', 'Hierro'), ('GRANCANARIA', 'GranCanaria'), ('FUERTEVENTURA', 'Fuerteventura'), ('LANZAROTE', 'Lanzarote')]),
        ),
    ]
