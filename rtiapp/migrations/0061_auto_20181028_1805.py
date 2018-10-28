# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0060_grupo_isla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='isla',
            field=models.CharField(max_length=15, default='NINGUNA', choices=[('NINGUNA', 'Ninguna'), ('TENERIFE', 'Tenerife'), ('GOMERA', 'Gomera'), ('PALMA', 'Palma'), ('HIERRO', 'Hierro'), ('GRANCANARIA', 'GranCanaria'), ('FUERTEVENTURA', 'Fuerteventura'), ('LANZAROTE', 'Lanzarote')]),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='isla',
            field=models.CharField(max_length=15, default='NINGUNA', choices=[('NINGUNA', 'Ninguna'), ('TENERIFE', 'Tenerife'), ('GOMERA', 'Gomera'), ('PALMA', 'Palma'), ('HIERRO', 'Hierro'), ('GRANCANARIA', 'GranCanaria'), ('FUERTEVENTURA', 'Fuerteventura'), ('LANZAROTE', 'Lanzarote')]),
        ),
    ]
