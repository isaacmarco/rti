# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0039_relaciongrupoevaluador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relaciongrupoevaluador',
            name='evaluador',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
