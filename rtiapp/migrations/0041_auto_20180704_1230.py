# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0040_auto_20180704_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubicacion',
            name='latitud',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ubicacion',
            name='longitud',
            field=models.FloatField(default=0),
        ),
    ]
