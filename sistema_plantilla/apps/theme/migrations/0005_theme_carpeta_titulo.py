# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0004_auto_20160108_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='carpeta_titulo',
            field=models.BooleanField(default=False),
        ),
    ]
