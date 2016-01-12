from django.db import models
from django.contrib.auth.models import User
from apps.theme_admin.models import ThemeAdmin


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.zip']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class Theme(models.Model):
    usuario = models.ForeignKey(User, related_name='user_theme')
    theme_titulo = models.CharField("Titulo", max_length=255, unique=True)
    estado = models.BooleanField("Estado", default=True)
    carpeta_titulo = models.CharField("Titulo de Carpeta", max_length=120, blank=True)
    comprimido = models.FileField(upload_to="theme", validators=[validate_file_extension])

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __str__(self):
        return "Theme elegido"


class ThemeActivo(models.Model):
    theme_admin = models.ForeignKey(ThemeAdmin, related_name='theme_admin_activo', null=True)
    theme = models.ForeignKey(Theme, related_name='theme_activo', null=True, unique=True)
    estado = models.BooleanField("Estado", default=False)

    class Meta:
        verbose_name = "ThemeActivo"
        verbose_name_plural = "ThemeActivos"

    def __str__(self):
        return "Theme elegido"
