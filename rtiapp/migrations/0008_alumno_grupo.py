# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0007_remove_alumno_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='grupo',
            field=models.ForeignKey(default=0, to='rtiapp.Grupo'),
        ),
    ]
