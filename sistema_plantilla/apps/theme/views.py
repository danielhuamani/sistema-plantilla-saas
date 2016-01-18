from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import ThemeForm
from os.path import join
from zipfile import ZipFile

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
            ZipFile(request.FILES.get('comprimido'), 'r')
            nombre_carpeta = ""
            error_template = False
            error_static = False
            error_imagen = False
            error_json = False
            mensaje = ""
            unziped = ZipFile(request.FILES.get('comprimido'), 'r')
            print unziped.namelist()
            for file_path in unziped.namelist():
                split_directorio = file_path.split("/")
                if split_directorio[0] != 'template' and split_directorio[0] != 'static':
                    if not nombre_carpeta:
                        nombre_carpeta = split_directorio[0]
                if split_directorio[1] == 'template' or split_directorio[0] == 'template':
                    archivo = unziped.extract(file_path, "templates/"+request.user.username+"/"+request.POST.get('theme_titulo'))
                    if not error_template:
                        error_template = True
                if split_directorio[1] == 'static' or split_directorio[0] == 'static':
                    # print "entro"
                    archivo = unziped.extract(file_path, "static/"+request.user.username+"/"+request.POST.get('theme_titulo'))
                    if not error_static:
                        error_static = True
            if error_static and error_template:
                theme = form.save()
                theme.carpeta_titulo = nombre_carpeta
                theme.save()
                mensaje = "Se Creo el theme Satisfactoriamente"
                return redirect(reverse_lazy("configuracion:home"))
            else:
                mensaje = "Hubo error posiblemente por que no tiene la carpeta template y static"
                # file_content = unziped.printdir()
            # print "----"
            # print file_path
            # print unziped.extract(file_path, "carpeta nueva/template")
    else:
        form = ThemeForm()
    return render(request, 'core/agregar_theme.html', locals())


