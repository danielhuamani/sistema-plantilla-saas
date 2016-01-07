from django.shortcuts import render
from django.conf import settings
from os.path import dirname, join, realpath
from os import listdir
import json
from PIL import Image


def home(request):
    print (settings.BASE_DIR)
    carpeta_templates = join(settings.BASE_DIR, 'templates')
    carpeta_static = join(settings.BASE_DIR, 'static')
    listado_themes = []
    listado_themes, env = lectura_themes(carpeta_templates, carpeta_static)
    return render(request, 'core/home.html', locals())


def variables(request):
    return render(request, 'core/variables.html', locals())


def lectura_themes(carpeta_templates, carpeta_static):
    templates = carpeta_templates
    static = carpeta_static
    listado_themes = []
    env = ""
    img = ""
    for x in listdir(templates):
        print (templates+'/'+x+'/init.json')
        try:
            img = Image.open(static+'/'+x+'/theme.png')
            dic_theme = {
                'imagen_url': "/"+x+'/theme.png',
                'titulo': x
            }
            listado_themes.append(dic_theme)
        except IOError as e:
            print ("error")
        try:
            with open(templates+'/'+x+'/init.json') as f:
                env = json.load(f)
        except IOError as e:
            print ("no existe el archivo init")
    return listado_themes, env
