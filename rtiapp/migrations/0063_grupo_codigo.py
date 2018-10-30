# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0062_evaluador_clave'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='codigo',
            field=models.CharField(max_length=50, default='Codigo del grupo'),
        ),
    ]
