# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0048_auto_20180709_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='informacion_adicional_completa',
            field=models.BooleanField(default=False),
        ),
    ]
