from django.db import models
from django.contrib.auth.models import User


class ThemeAdmin(models.Model):
    usuario = models.ForeignKey(User, related_name='user_theme_admin')
    theme_titulo = models.CharField("Titulo", max_length=255, unique=True)
    estado = models.BooleanField("Estado", default=True)

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __str__(self):
        return self.theme_titulo
