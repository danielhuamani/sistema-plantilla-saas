# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0005_theme_carpeta_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='carpeta_titulo',
            field=models.CharField(max_length=120, verbose_name=b'Titulo de Carpeta', blank=True),
        ),
    ]
