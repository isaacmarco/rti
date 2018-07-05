# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0005_auto_20180621_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='grupo',
            field=models.IntegerField(default=0),
        ),
    ]
