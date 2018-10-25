# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0055_auto_20181010_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='CFS_ACIERTOS',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='CFS_TIEMPO',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='CLE_TEXTO_ACIERTOS',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='CLE_TEXTO_TIEMPO',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='CSL_ACIERTOS',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='CSL_TIEMPO',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='VOC_ACIERTOS',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='VOC_TIEMPO',
        ),
    ]
