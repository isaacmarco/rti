# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0009_auto_20180622_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='pais',
            field=models.CharField(max_length=3, default='ESP', choices=[('ESP', 'España'), ('GTM', 'Guatemala'), ('ECU', 'Ecuador'), ('CAN', 'Canarias')]),
        ),
        migrations.AlterField(
            model_name='evaluador',
            name='pais',
            field=models.CharField(max_length=3, default='ESP', choices=[('ESP', 'España'), ('GTM', 'Guatemala'), ('ECU', 'Ecuador'), ('CAN', 'Canarias')]),
        ),
    ]
