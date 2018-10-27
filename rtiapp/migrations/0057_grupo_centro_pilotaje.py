# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0056_auto_20181025_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='centro_pilotaje',
            field=models.CharField(max_length=50, default='Centro pilotaje'),
        ),
    ]
