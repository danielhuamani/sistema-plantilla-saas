# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0007_theme_comprimido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themeactivo',
            name='theme',
            field=models.ForeignKey(related_name='theme_activo', blank=True, to='theme.Theme', null=True),
        ),
        migrations.AlterField(
            model_name='themeactivo',
            name='theme_admin',
            field=models.ForeignKey(related_name='theme_admin_activo', blank=True, to='theme_admin.ThemeAdmin', null=True),
        ),
    ]
