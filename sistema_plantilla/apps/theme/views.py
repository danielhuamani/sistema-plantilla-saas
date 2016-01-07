from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
import os
from os.path import join


class UsuarioCreate(CreateView):
    model = User
    fields = ['username', 'password']
    template_name = 'core/registrar.html'
    success_url = reverse_lazy("configuracion:home")

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        carpeta_templates = join(settings.BASE_DIR, 'templates')
        carpeta_static = join(settings.BASE_DIR, 'static')
        self.object = form.save()
        os.mkdir(carpeta_templates+"/"+self.object.username)
        os.mkdir(carpeta_static+"/"+self.object.username)

        return super(UsuarioCreate, self).form_valid(form)

# def registrar(request):
#     return render(request, 'core/registrar.html', locals())
