from django.shortcuts import render
from .models import Producto, Categoria


def home(request):
    template = 'default/home.html'
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, template, locals())


def productos(request):
    template = 'default/productos.html'
    return render(request, template, locals())

