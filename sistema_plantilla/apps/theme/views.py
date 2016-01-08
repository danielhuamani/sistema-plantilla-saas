from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import ThemeForm
import os
from os.path import join
from zipfile import ZipFile
import StringIO
import shutil


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


def agregar_theme(request):
    if request.method == "POST":
        form = ThemeForm(request.POST, request.FILES)
        if form.is_valid():
            # theme = form.save()
            # creacion_carpetas(request.user.username, theme.theme_titulo)
            unziped = ZipFile(request.FILES.get('theme_comprimido'), 'r')
            print StringIO.StringIO(unziped)
            print unziped
            # with ZipFile(unziped) as f:
            #     try:
            #         f.extractall(PATH, pwd=pwd)
            #     except RuntimeError:
            #         pwd = raw_input("Clave para %s: " % filename)
            #         decompress(FIELDNAME = forms.URLField()ilename, pwd=pwd)
            print unziped.namelist()
            for file_path in unziped.namelist():
                split_template = file_path.split("/")
                if split_template[1] == 'template':
                    print "entro"
                    archivo = unziped.extract(file_path, "templates/"+request.user.username+"/"+request.POST.get('theme_titulo'))
                    shutil.move(archivo, join(settings.BASE_DIR, 'templates') + "/" + request.user.username + "/" + "te")

                # file_content = unziped.printdir()
            # print "----"
            # print file_path
            # print unziped.extract(file_path, "carpeta nueva/template")
    else:
        form = ThemeForm()
    return render(request, 'core/agregar_theme.html', locals())


def creacion_carpetas(username, nombre_carpeta):
    carpeta_templates = join(settings.BASE_DIR, 'templates') + "/" + username
    carpeta_static = join(settings.BASE_DIR, 'static') + "/" + username
    os.mkdir(carpeta_templates+"/"+nombre_carpeta)
    os.mkdir(carpeta_static+"/"+nombre_carpeta)
    return False
