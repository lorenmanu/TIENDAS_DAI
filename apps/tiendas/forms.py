from django import forms
from .models import Tienda, Zona, UserProfile
from django.contrib.auth.models import User



class ZonaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Introduce nombre de la zona nueva.")
    localizacion = forms.CharField(max_length=128, help_text="Introduce en que zona del mapa se localiza, ejemplo:Norte Granada....")
    model = Zona
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Zona
        exclude = ('views','slug')


class TiendaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Por favor mete el nombre de la tienda.")
    calle = forms.CharField(max_length=128, help_text="Intoduce donde se localiza.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tienda
        exclude = ('zona','views','slug')


class UserForm(forms.ModelForm):
    username = forms.SlugField (max_length=8, label='Nombre de usuario:')
    email    = forms.EmailField (label='Correo:')
    password = forms.SlugField (max_length=8, 
                       help_text="(Hasta 8 caracteres)", 
                       widget=forms.PasswordInput(),  
                       label='Contrasena:')
    class Meta:
        model  = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)