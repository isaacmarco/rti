# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0016_auto_20180623_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluacion_ipal_infantil',
            old_name='ADI',
            new_name='ADIVINANZAS',
        ),
        migrations.RemoveField(
            model_name='evaluacion_ipal_infantil',
            name='GLOBAL',
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_primero',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_segundo',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipae_tercero',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_infantil',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_primero',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipal_segundo',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_infantil',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_primero',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_segundo',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='momento',
            field=models.CharField(max_length=3, default='INI', choices=[('INI', 'Inicio'), ('MED', 'Medio'), ('FIN', 'FIn')]),
        ),
        migrations.AddField(
            model_name='evaluacion_ipam_tercero',
            name='omnibus',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=10),
        ),
    ]
