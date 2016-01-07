from django.db import models
from django.contrib.auth.models import User


class Theme(models.Model):
    usuario = models.ForeignKey(User, related_name='user_theme')
    theme_titulo = models.CharField("Titulo", max_length=255)

    class Meta:
        verbose_name = "Theme"
        verbose_name_plural = "Themes"

    def __str__(self):
        pass
