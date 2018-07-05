# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0037_auto_20180703_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='curso_academico',
            field=models.IntegerField(default=2018),
        ),
    ]
