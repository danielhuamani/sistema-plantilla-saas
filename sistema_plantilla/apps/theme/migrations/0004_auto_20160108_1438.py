# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_themeactivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='theme_titulo',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='themeactivo',
            name='theme',
            field=models.ForeignKey(related_name='theme_activo', null=True, to='theme.Theme', unique=True),
        ),
    ]
