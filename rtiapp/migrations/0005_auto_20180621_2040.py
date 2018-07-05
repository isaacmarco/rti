# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0004_auto_20180621_2028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relaciongrupoalumno',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='relaciongrupoalumno',
            name='grupo',
        ),
        migrations.AddField(
            model_name='alumno',
            name='grupo',
            field=models.ForeignKey(default=0, to='rtiapp.Grupo'),
        ),
        migrations.DeleteModel(
            name='RelacionGrupoAlumno',
        ),
    ]
