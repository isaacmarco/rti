# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0003_auto_20180621_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grupo',
            old_name='nombre_grupo',
            new_name='nombre',
        ),
    ]
