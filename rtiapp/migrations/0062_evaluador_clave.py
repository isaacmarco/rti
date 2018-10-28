# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0061_auto_20181028_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='clave',
            field=models.CharField(max_length=20, default='Clave del evaluador'),
        ),
    ]
