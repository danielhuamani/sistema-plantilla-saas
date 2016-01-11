from django import forms
from .models import Theme


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ('usuario', 'theme_titulo', 'carpeta_titulo')
