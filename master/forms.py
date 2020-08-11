from django.forms import ModelForm
from django import forms
from .models import *

class KategoriForm(ModelForm):
    class Meta:
        model = KategoriPengaduan
        fields = '__all__'
