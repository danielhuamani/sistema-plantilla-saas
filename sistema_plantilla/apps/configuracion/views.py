from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from apps.theme.models import Theme, ThemeActivo
from apps.theme.forms import ThemeActivoForm
from os.path import join
from os import listdir
import json
from PIL import Image


def home(request):
    usuario = request.user
    my_themes = Theme.objects.filter(usuario=usuario, estado=True).prefetch_related("theme_activo")
    theme_activo = ThemeActivo.objects.filter(estado=True)[0]
    estado_activo_admin = ""
    estado_activo = ""
    if theme_activo.theme_admin:
        estado_activo_admin = theme_activo.theme_admin.theme_titulo
    if theme_activo.theme:
        estado_activo = theme_activo.theme.theme_titulo
    carpeta_templates = join(settings.BASE_DIR, 'templates')
    carpeta_static = join(settings.BASE_DIR, 'static')
    listado_themes, env = lectura_themes_core(carpeta_templates, carpeta_static)
    listado_my_themes = lectura_themes_usuario(carpeta_templates, carpeta_static, my_themes, usuario.username)
    if request.method == "POST":
        form = ThemeActivoForm(request.POST)
        if form.is_valid():
            ThemeActivo.objects.filter(estado=True).update(estado=False)
            agregar_estado = form.save(commit=False)
            agregar_estado.estado = True
            agregar_estado.save()
        else:
            print "error"

    else:
        form = ThemeActivoForm()
    return render(request, 'core/home.html', locals())


def variables(request):
    return render(request, 'core/variables.html', locals())


def lectura_themes_core(carpeta_templates, carpeta_static):
    templates = carpeta_templates
    static = carpeta_static
    listado_themes = []
    env = ""
    img = ""
    for x in listdir(templates):
        try:
            img = Image.open(static+'/'+x+'/theme.png')
            dic_theme = {
                'imagen_url': "/"+x+'/theme.png',
                'titulo': x
            }
            listado_themes.append(dic_theme)
        except IOError as e:
            pass
        try:
            with open(templates+'/'+x+'/conf.json') as f:
                env = json.load(f)
        except IOError as e:
            pass
    return listado_themes, env


def lectura_themes_usuario(carpeta_templates, carpeta_static, modelo_theme, usuario):
    usuario = usuario
    templates = carpeta_templates
    static = carpeta_static
    modelo_theme = modelo_theme
    listado_themes = []
    env = ""
    img = ""
    for theme in modelo_theme:
        if theme.carpeta_titulo:
            carpeta_titulo = theme.carpeta_titulo

            try:
                img = Image.open(static + '/' + usuario + "/" + theme.theme_titulo + "/" + carpeta_titulo + "/static/theme.png")
                dic_theme = {
                    'imagen_url': "/"+usuario+"/"+theme.theme_titulo+"/"+carpeta_titulo+"/static/theme.png",
                    'titulo': theme.theme_titulo,
                    'theme_pk': theme.pk
                }
                listado_themes.append(dic_theme)
            except IOError as e:
                print ("error 1")
        else:
            try:
                img = Image.open(static+'/'+usuario+"/"+theme.theme_titulo+'/static/theme.png')
                dic_theme = {
                    'imagen_url': "/"+usuario+"/"+theme.theme_titulo+'/static/theme.png',
                    'titulo': theme.theme_titulo,
                    'theme_pk': theme.pk
                }
                listado_themes.append(dic_theme)
            except IOError as e:
                print ("error")
        # print (templates+'/'+x+'/init.json')
        # try:
        #     with open(templates+'/'+usuario+'/conf.json') as f:
        #         env = json.load(f)
        # except IOError as e:
        #     print ("no existe el archivo init")
    return listado_themes


def consultar_json_theme(usuario):
    usuario = usuario.username
    carpeta_template = join(settings.BASE_DIR, 'templates')
    carpeta_static = join(settings.BASE_DIR, 'static')
    theme_activo = ThemeActivo.objects.filter(estado=True)[0]
    theme_elegido = ""
    carpeta_elegida = ""
    ruta_template = ""
    if theme_activo.theme_admin:
        theme_elegido = theme_activo.theme_admin.theme_titulo

    if theme_activo.theme:
        theme_elegido = theme_activo.theme.theme_titulo
        carpeta_elegida = theme_activo.theme.carpeta_titulo
    if carpeta_elegida:
        ruta_template = carpeta_template+"/"+usuario+"/"+theme_elegido+"/"+carpeta_elegida+"/template/"
        ruta_static = settings.STATIC_URL+usuario+"/"+theme_elegido+"/"+carpeta_elegida+"/static/"
    else:
        ruta_template = carpeta_template+"/"+usuario+"/"+theme_elegido+"/template/"
        ruta_static = settings.STATIC_URL+usuario+"/"+theme_elegido+"/static/"
    print "555555"
    print ruta_static
    with open(ruta_template+"/conf.json") as f:
        return json.load(f), ruta_template, ruta_static
    return {}
