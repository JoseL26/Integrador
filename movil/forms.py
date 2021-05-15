from django import forms
from .models import Categoria, Cargo
class FormularioEmpleado(forms.Form):
    Apellidos = forms.CharField(min_length="6")
    Nombres= forms.CharField(min_length="3")
    DNI= forms.IntegerField()
    Direccion=forms.CharField()
    Distrito=forms.CharField()
    Provincia=forms.CharField(max_length="20", min_length="3")
    Telefono=forms.IntegerField(required=True)
    Correo=forms.EmailField(required=True)
    Categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
    Cargo=forms.ModelChoiceField(queryset=Cargo.objects.all())
    Estado=forms.IntegerField()