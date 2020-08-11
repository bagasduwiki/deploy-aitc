from django.forms import ModelForm
from django import forms
from .models import *

class PelayananForm(ModelForm):
    class Meta:
        model = Pengaduans
        fields = '__all__'

class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'

class DeletePelayananForm(ModelForm):
    class Meta:
        model = Pengaduans
        fields = '__all__'

class JawabForm(ModelForm):
    class Meta:
        model = Respons
        fields = '__all__'

class StatusForm(ModelForm):
    class Meta:
        model = Pengaduans
        fields = ['kategori_penanganan']

class EditStatusForm(ModelForm):
	pk = forms.IntegerField()
	class Meta:
		model = Pengaduans
		fields = '__all__'

class FilterForm(forms.Form):
    KATEGORI=(
        ('', '------------'),
        ("TKP", "TKP"),
        ("Online","Online"),
        ("Selesai","Selesai"),
    )
    kategori_penanganan = forms.ChoiceField(choices=KATEGORI, required=False)
