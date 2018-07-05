# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0042_grupo_evaluadores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relaciongrupoevaluador',
            name='evaluador',
        ),
        migrations.RemoveField(
            model_name='relaciongrupoevaluador',
            name='grupo',
        ),
        migrations.DeleteModel(
            name='RelacionGrupoEvaluador',
        ),
    ]
