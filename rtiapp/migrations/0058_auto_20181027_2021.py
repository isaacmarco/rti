# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0057_grupo_centro_pilotaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='CFS',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(85), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='CSL',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='VOC',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(0)]),
        ),
    ]
