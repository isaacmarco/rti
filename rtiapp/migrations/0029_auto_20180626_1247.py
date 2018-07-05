# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0028_auto_20180625_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluador',
            name='email',
            field=models.EmailField(max_length=254, default='email@email.com'),
        ),
        migrations.AlterField(
            model_name='evaluador',
            name='centro',
            field=models.CharField(max_length=50, default='Centro del evaluador'),
        ),
        migrations.AlterField(
            model_name='evaluador',
            name='nombre',
            field=models.CharField(max_length=50, default='Nombre del evaluador'),
        ),
    ]
