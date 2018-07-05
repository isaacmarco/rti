# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rtiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_grupo', models.CharField(max_length=100, default='Nombre del grupo')),
                ('curso', models.CharField(max_length=2, default='IN', choices=[('IN', 'Infantil'), ('PR', 'Primero'), ('SG', 'Segundo'), ('TR', 'Tercero')])),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='relaciongruposevaluadores',
            name='evaluador',
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso',
            field=models.CharField(max_length=2, default='IN', choices=[('IN', 'Infantil'), ('PR', 'Primero'), ('SG', 'Segundo'), ('TR', 'Tercero')]),
        ),
        migrations.DeleteModel(
            name='RelacionGruposEvaluadores',
        ),
    ]
