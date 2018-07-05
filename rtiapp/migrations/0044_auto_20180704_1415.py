# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0043_auto_20180704_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='evaluadores',
            field=models.ManyToManyField(related_name='Evaluadores', to=settings.AUTH_USER_MODEL),
        ),
    ]
