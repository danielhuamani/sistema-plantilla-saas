from django.shortcuts import render
from .models import Producto, Categoria
from apps.configuracion.views import consultar_json_theme


def home(request):
    env_temp, ruta_template, ruta_static = consultar_json_theme(request.user)
    if env_temp:
        dir_template = env_temp.get('HOME')
        template = ruta_template + dir_template
        STATIC_URL = ruta_static
        # print STATIC_URL
    else:
        template = 'default/home.html'
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, template, locals())


def productos(request):
    template = 'default/productos.html'
    return render(request, template, locals())
