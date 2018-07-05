# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0041_auto_20180704_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='evaluadores',
            field=models.ManyToManyField(to='rtiapp.Evaluador'),
        ),
    ]
