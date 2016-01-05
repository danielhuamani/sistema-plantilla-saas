from django.db import models


class Categoria(models.Model):
    categoria_titulo = models.CharField('Titulo', max_length=100)
    categoria_descripcion = models.TextField('Descripcion')
    categoria_estado = models.BooleanField('Estado', default=True)
    categoria_fecha_ingreso = models.DateTimeField('Fecha Ingreso', auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria_titulo


class Producto(models.Model):
    categoria = models.ManyToManyField(Categoria, related_name='categoria_producto')
    producto_sku = models.CharField('SKU', max_length=120, unique=True, db_index=True)
    producto_titulo = models.CharField('Titulo', max_length=250)
    producto_descripcion = models.TextField('Descripcion')
    producto_precio = models.DecimalField('Precio', max_digits=12, decimal_places=2)
    producto_cantidad = models.IntegerField('Cantidad')
    producto_estado = models.BooleanField('Estado', default=True)
    producto_fecha_ingreso = models.DateTimeField('Fecha Ingreso', auto_now_add=True)
    producto_estado_eliminado = models.BooleanField('Estado Eliminado', default=False)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.producto_titulo


class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, related_name='producto_productoimagen')
    producto_imagen_contenido = models.ImageField('Producto Imagen', upload_to='producto/', max_length=250)
    producto_imagen_posicion = models.IntegerField('Posicion', default=0)

    class Meta:
        verbose_name = "Producto Imagen"
        verbose_name_plural = "Producto Imagenes"

    def __str__(self):
        return str(self.producto)
