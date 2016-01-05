# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('producto_imagen_contenido', models.ImageField(max_length=250, verbose_name='Producto Imagen', upload_to='producto/')),
                ('producto_imagen_posicion', models.IntegerField(verbose_name='Posicion', default=0)),
                ('producto', models.ForeignKey(to='productos.Producto', related_name='producto_productoimagen')),
            ],
            options={
                'verbose_name': 'Producto Imagen',
                'verbose_name_plural': 'Producto Imagenes',
            },
        ),
    ]
