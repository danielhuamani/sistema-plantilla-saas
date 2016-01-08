# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme_admin', '0001_initial'),
        ('theme', '0002_theme_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeActivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.BooleanField(default=False, verbose_name=b'Estado')),
                ('theme', models.ForeignKey(related_name='theme_activo', to='theme.Theme', null=True)),
                ('theme_admin', models.ForeignKey(related_name='theme_admin_activo', to='theme_admin.ThemeAdmin', null=True)),
            ],
            options={
                'verbose_name': 'ThemeActivo',
                'verbose_name_plural': 'ThemeActivos',
            },
        ),
    ]
