# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100, default='Nombre del alumno')),
                ('pais', models.CharField(max_length=100, default='España')),
                ('fecha_nacimiento', models.IntegerField(default=0)),
                ('centro', models.CharField(max_length=100, default='Centro')),
                ('sexo', models.CharField(max_length=2, default='HM', choices=[('HM', 'Hombre'), ('MJ', 'Mujer')])),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAE_PRIMERO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('TLC_1', models.IntegerField(default=0)),
                ('DICTADO_ORTOGRAFIA_ARBITRARIA', models.IntegerField(default=0)),
                ('DICTADO_ORTOGRAFIA_REGLADA', models.IntegerField(default=0)),
                ('DICTADO_PSEUDOPALABRAS', models.IntegerField(default=0)),
                ('DICTADO_FRASES', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAE_SEGUNDO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('TLC_1', models.IntegerField(default=0)),
                ('DICTADO_ORTOGRAFIA_ARBITRARIA', models.IntegerField(default=0)),
                ('DICTADO_ORTOGRAFIA_REGLADA', models.IntegerField(default=0)),
                ('DICTADO_PSEUDOPALABRAS', models.IntegerField(default=0)),
                ('DICTADO_FRASES', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAE_TERCERO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('DICTADO_ORTOGRAFIA_ARBITRARIA', models.IntegerField(default=0)),
                ('DICTADO_ORTOGRAFIA_REGLADA', models.IntegerField(default=0)),
                ('DICTADO_FRASES', models.IntegerField(default=0)),
                ('SEC_5', models.IntegerField(default=0)),
                ('SEC_SEI_5', models.IntegerField(default=0)),
                ('PDC_5', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAL_INFANTIL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('ADI', models.IntegerField(default=0)),
                ('CSL', models.IntegerField(default=0)),
                ('CNL', models.IntegerField(default=0)),
                ('CLE_IMAGEN', models.IntegerField(default=0)),
                ('CLE_TEXTO', models.IntegerField(default=0)),
                ('CFA', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAL_PRIMERO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('TM', models.IntegerField(default=0)),
                ('LP', models.IntegerField(default=0)),
                ('CSL', models.IntegerField(default=0)),
                ('CNL', models.IntegerField(default=0)),
                ('FLO', models.IntegerField(default=0)),
                ('CLE_TEXTO', models.IntegerField(default=0)),
                ('CFS', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAL_SEGUNDO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('CNL', models.IntegerField(default=0)),
                ('LP', models.IntegerField(default=0)),
                ('TM', models.IntegerField(default=0)),
                ('FLO', models.IntegerField(default=0)),
                ('PRO', models.IntegerField(default=0)),
                ('CSL', models.IntegerField(default=0)),
                ('CLE_TEXTO', models.IntegerField(default=0)),
                ('CFS', models.IntegerField(default=0)),
                ('VOC', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAM_INFANTIL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('CN', models.IntegerField(default=0)),
                ('EC', models.IntegerField(default=0)),
                ('SN', models.IntegerField(default=0)),
                ('IN', models.IntegerField(default=0)),
                ('CVA', models.IntegerField(default=0)),
                ('CM', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAM_PRIMERO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('CN', models.IntegerField(default=0)),
                ('ODD', models.IntegerField(default=0)),
                ('SN', models.IntegerField(default=0)),
                ('OUD', models.IntegerField(default=0)),
                ('VP', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAM_SEGUNDO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('CN', models.IntegerField(default=0)),
                ('ODD', models.IntegerField(default=0)),
                ('SN', models.IntegerField(default=0)),
                ('OUD', models.IntegerField(default=0)),
                ('VP', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluacion_IPAM_TERCERO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_alumno', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=2, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')])),
                ('CN', models.IntegerField(default=0)),
                ('ODD', models.IntegerField(default=0)),
                ('SN', models.IntegerField(default=0)),
                ('OUD', models.IntegerField(default=0)),
                ('VP', models.IntegerField(default=0)),
                ('GLOBAL', models.IntegerField(default=0)),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Evaluador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=100, default='Nombre del evaluador')),
                ('centro', models.CharField(max_length=100, default='Centro del evaluador')),
                ('pais', models.CharField(max_length=2, default='ESP', choices=[('ESP', 'España'), ('GTM', 'Guatemala'), ('ECU', 'Ecuador'), ('CAN', 'Canarias')])),
                ('sexo', models.CharField(max_length=2, default='HM', choices=[('HM', 'Hombre'), ('MJ', 'Mujer')])),
                ('nivel_academico', models.CharField(max_length=2, default='GR', choices=[('DP', 'Diplomatura'), ('LC', 'Licenciatura'), ('GR', 'Grado'), ('MT', 'Master'), ('DC', 'Doctorado')])),
                ('profesion', models.CharField(max_length=2, default='MS', choices=[('OR', 'Orientador'), ('PS', 'Psicologo'), ('PG', 'Pedagogo'), ('SG', 'Psicopedagogo'), ('MS', 'Maestro')])),
                ('zona', models.CharField(max_length=2, default='UB', choices=[('PR', 'Periferia'), ('UB', 'Urbana'), ('RU', 'Rural')])),
            ],
            options={
                'verbose_name': 'Evaluador',
                'verbose_name_plural': 'Evaluadores',
            },
        ),
        migrations.CreateModel(
            name='RelacionGruposEvaluadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_grupo', models.CharField(max_length=100, default='Nombre del grupo')),
                ('evaluador', models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
