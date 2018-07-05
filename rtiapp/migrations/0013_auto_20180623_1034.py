# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0012_auto_20180623_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='mes',
            field=models.CharField(max_length=20, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo'), ('JUN', 'Junio')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='tipo',
            field=models.CharField(max_length=20, default='EV', choices=[('EV', 'Evaluacion'), ('PR', 'Progreso')]),
        ),
    ]
