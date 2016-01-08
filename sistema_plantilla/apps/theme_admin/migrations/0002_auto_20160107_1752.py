# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='themeadmin',
            name='theme_titulo',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'Titulo'),
        ),
    ]
