# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='estado',
            field=models.BooleanField(default=True, verbose_name=b'Estado'),
        ),
    ]
