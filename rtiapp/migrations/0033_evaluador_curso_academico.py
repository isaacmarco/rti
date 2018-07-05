# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0032_auto_20180627_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
    ]
