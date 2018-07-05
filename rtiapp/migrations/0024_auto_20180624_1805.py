# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0023_auto_20180624_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='mes_intero',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
    ]
