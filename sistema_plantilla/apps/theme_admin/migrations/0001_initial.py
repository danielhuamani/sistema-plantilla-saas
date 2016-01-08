# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theme_titulo', models.CharField(max_length=255, verbose_name=b'Titulo')),
                ('estado', models.BooleanField(default=True, verbose_name=b'Estado')),
                ('usuario', models.ForeignKey(related_name='user_theme_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Theme',
                'verbose_name_plural': 'Themes',
            },
        ),
    ]
