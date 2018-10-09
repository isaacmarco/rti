# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0053_auto_20180713_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='centro_pilotaje',
            field=models.CharField(max_length=50, default='Centro pilotaje'),
        ),
    ]
