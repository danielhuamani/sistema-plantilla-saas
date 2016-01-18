from django import forms
from .models import Theme, ThemeActivo


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('usuario', 'theme_titulo', 'carpeta_titulo', 'comprimido')


class ThemeActivoForm(forms.ModelForm):
    class Meta:
        model = ThemeActivo
        fields = ('theme_admin', 'theme', 'estado')
