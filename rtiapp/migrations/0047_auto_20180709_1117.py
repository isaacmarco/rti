# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0046_auto_20180709_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
