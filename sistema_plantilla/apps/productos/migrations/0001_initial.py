# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('categoria_titulo', models.CharField(verbose_name='Titulo', max_length=100)),
                ('categoria_descripcion', models.TextField(verbose_name='Descripcion')),
                ('categoria_estado', models.BooleanField(verbose_name='Estado', default=True)),
                ('categoria_fecha_ingreso', models.DateTimeField(verbose_name='Fecha Ingreso', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('producto_sku', models.CharField(verbose_name='SKU', db_index=True, unique=True, max_length=120)),
                ('producto_titulo', models.CharField(verbose_name='Titulo', max_length=250)),
                ('producto_descripcion', models.TextField(verbose_name='Descripcion')),
                ('producto_precio', models.DecimalField(decimal_places=2, verbose_name='Precio', max_digits=12)),
                ('producto_cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('producto_estado', models.BooleanField(verbose_name='Estado', default=True)),
                ('producto_fecha_ingreso', models.DateTimeField(verbose_name='Fecha Ingreso', auto_now_add=True)),
                ('producto_estado_eliminado', models.BooleanField(verbose_name='Estado Eliminado', default=False)),
                ('categoria', models.ManyToManyField(related_name='categoria_producto', to='productos.Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
