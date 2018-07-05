# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rtiapp', '0035_auto_20180628_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emblema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tipo', models.IntegerField(default=2018)),
                ('fecha', models.IntegerField(default=2018)),
            ],
        ),
        migrations.CreateModel(
            name='Explorador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=10, default='noviembre')),
                ('puntuacion', models.IntegerField(default=2018)),
                ('usuario', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=10, default='noviembre')),
                ('latitud', models.IntegerField(default=2018)),
                ('longitud', models.IntegerField(default=2018)),
            ],
        ),
        migrations.AddField(
            model_name='emblema',
            name='explorador',
            field=models.ForeignKey(default=0, to='rtiapp.Explorador'),
        ),
        migrations.AddField(
            model_name='emblema',
            name='ubicacion',
            field=models.ForeignKey(default=0, to='rtiapp.Ubicacion'),
        ),
    ]
