# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0030_auto_20180626_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='CFS_ACIERTOS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='CFS_TIEMPO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='CLE_TEXTO_ACIERTOS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='CLE_TEXTO_TIEMPO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='CSL_ACIERTOS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='CSL_TIEMPO',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='VOC_ACIERTOS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='VOC_TIEMPO',
            field=models.IntegerField(default=0),
        ),
    ]
