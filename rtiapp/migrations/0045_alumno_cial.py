# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0044_auto_20180704_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='CIAL',
            field=models.CharField(max_length=100, default='XXX-XXX'),
        ),
    ]
