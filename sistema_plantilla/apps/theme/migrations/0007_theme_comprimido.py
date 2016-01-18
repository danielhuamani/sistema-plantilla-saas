# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.theme.models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_auto_20160111_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='comprimido',
            field=models.FileField(default='', upload_to=b'theme', validators=[apps.theme.models.validate_file_extension]),
            preserve_default=False,
        ),
    ]
