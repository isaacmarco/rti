# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0002_auto_20180619_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelacionGrupoAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.AlterField(
            model_name='alumno',
            name='curso',
            field=models.CharField(max_length=20, default='INFANTIL', choices=[('INFANTIL', 'Infantil'), ('PRIMARIA', 'Primero'), ('SEGUNDO', 'Segundo'), ('TERCERO', 'Tercero')]),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='curso',
            field=models.CharField(max_length=20, default='INFANTIL', choices=[('INFANTIL', 'Infantil'), ('PRIMARIA', 'Primero'), ('SEGUNDO', 'Segundo'), ('TERCERO', 'Tercero')]),
        ),
        migrations.AddField(
            model_name='relaciongrupoalumno',
            name='alumno',
            field=models.ForeignKey(default=0, to='rtiapp.Alumno'),
        ),
        migrations.AddField(
            model_name='relaciongrupoalumno',
            name='grupo',
            field=models.ForeignKey(default=0, to='rtiapp.Grupo'),
        ),
    ]
