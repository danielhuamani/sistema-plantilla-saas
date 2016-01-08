from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registrar/$', views.UsuarioCreate.as_view(), name='registrar'),
    url(r'^agregar-theme/$', views.agregar_theme, name='agregar_theme'),
]
