# -*- coding: utf-8 -*-

from django import template
from apps.configuracion.views import consultar_json_theme
register = template.Library()
from django.template import Library, loader, Context
from django.conf import settings
from os.path import join


@register.simple_tag(takes_context=True)
def header(context):
    print context['request']
    carpeta_tempalte = join(settings.BASE_DIR, 'templates')
    t = loader.get_template(carpeta_tempalte+"/juan/template_default/template_default/template/header.html")
    return t.render(Context({
        'STATIC_URL': settings.STATIC_URL+"juan/template_default/template_default/static/"
    }))


@register.simple_tag(takes_context=True)
def footer(context):

    carpeta_tempalte = join(settings.BASE_DIR, 'templates')
    t = loader.get_template(carpeta_tempalte+"/juan/template_default/template_default/template/footer.html")
    return t.render(Context({
        'STATIC_URL': settings.STATIC_URL+"juan/template_default/template_default/static/"
    }))
# HEADER
# @register.inclusion_tag('common/_header.html')
# def header():

#     return locals()


# # FOOTER
# @register.inclusion_tag('common/_footer.html')
# def footer():

#     return locals()

