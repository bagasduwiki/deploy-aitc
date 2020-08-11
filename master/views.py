from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from .models import *
from .forms import *

from aitc_service.views import *
from aitc_service.forms import *

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def kategori(request):
    kategori = KategoriPengaduan.objects.all()
    form = KategoriForm()
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('kategori')

    context = {'kategori':kategori, 'act':'kategori', 'form':form}
    return render(request, 'kategori.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def editkategori(request, pk):
    kategori = KategoriPengaduan.objects.get(id=pk)
    form = KategoriForm(instance=kategori)
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('kategori')

    context = {'form':form, 'kategori':kategori, 'act':'kategori'}
    return render(request, 'editkategori.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def kategoridel(request, pk):
    kategori = KategoriPengaduan.objects.get(id=pk)
    if request.method == 'POST':
        kategori.delete()
        messages.success(request, 'Data Berhasil Dihapus')
        return redirect('kategori')
