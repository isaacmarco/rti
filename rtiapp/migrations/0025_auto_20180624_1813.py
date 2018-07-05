# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0024_auto_20180624_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion_ipae_primero',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_segundo',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipae_tercero',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_infantil',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_primero',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_segundo',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_infantil',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_primero',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_segundo',
            name='mes_intero',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipam_tercero',
            name='mes_intero',
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='mes',
            field=models.IntegerField(default=1, choices=[(1, 'Noviembre'), (2, 'Diciembre'), (3, 'Enero'), (4, 'Febrero'), (5, 'Marzo'), (6, 'Abril'), (7, 'Mayo')]),
        ),
    ]
