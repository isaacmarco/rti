# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0017_auto_20180623_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='riesgo',
            field=models.CharField(max_length=4, default='NOEV', choices=[('NOEV', 'Sin evaluar'), ('RIES', 'Riesgo'), ('BAJO', 'Rendimiento bajo'), ('NORM', 'Rendimiento normal'), ('OPTI', 'Rendimiento optimo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_primero',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_segundo',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipae_tercero',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_infantil',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_primero',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipal_segundo',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_infantil',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_primero',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_segundo',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='mes',
            field=models.CharField(max_length=3, default='NOV', choices=[('NOV', 'Noviembre'), ('DIC', 'Diciembre'), ('ENE', 'Enero'), ('FEB', 'Febrero'), ('MAR', 'Marzo'), ('ABR', 'Abril'), ('MAY', 'Mayo')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='momento',
            field=models.CharField(max_length=10, default='INICIO', choices=[('INICIO', 'Inicio'), ('MEDIO', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AlterField(
            model_name='evaluacion_ipam_tercero',
            name='tipo',
            field=models.CharField(max_length=3, default='CR', choices=[('CR', 'Cribado'), ('PR', 'Progreso')]),
        ),
    ]
