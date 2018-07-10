# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0049_evaluador_informacion_adicional_completa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emblema',
            name='explorador',
        ),
        migrations.RemoveField(
            model_name='emblema',
            name='ubicacion',
        ),
        migrations.RemoveField(
            model_name='explorador',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Emblema',
        ),
        migrations.DeleteModel(
            name='Explorador',
        ),
        migrations.DeleteModel(
            name='Ubicacion',
        ),
    ]
