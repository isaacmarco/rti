# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0038_alumno_curso_academico'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelacionGrupoEvaluador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('evaluador', models.ForeignKey(default=0, to='rtiapp.Evaluador')),
                ('grupo', models.ForeignKey(default=0, to='rtiapp.Grupo')),
            ],
        ),
    ]
