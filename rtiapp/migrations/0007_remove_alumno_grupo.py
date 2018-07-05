# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0006_auto_20180621_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='grupo',
        ),
    ]
