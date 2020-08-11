from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from aitc_service.views import *
from aitc_service.forms import *
from .models import *
from .forms import *

###############Admin########################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def accounts(request):
    admin = request.user.admin
    form = AdminForm(instance=admin)

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')

    context = {'form':form, 'act':'accounts'}
    return render(request, 'akun.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tambahadmin(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='admin')
            user.groups.add(group)
            # Admin.objects.create(
            #     user=user,
            # )

            messages.success(request, 'Username telah ditambahkan untuk ' + username)
            return redirect('tambahdata')

    context = {'form':form, 'act':'admin'}
    return render(request, 'tambahadmin.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tambahdata(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin Telah Ditambahkan')
            return redirect('accounts')

    context = {'form':form, 'act':'admin'}
    return render(request, 'dataadmin.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ubahpassword(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            user.set_password(password_1)
            user.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('accounts')

    context = {'form':form, 'act':'accounts'}
    return render(request, 'ubahpassword.html', context)

###############Klien########################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def daftarclient(request):
    client = Client.objects.all()

    context = {'client':client, 'act':'klien'}
    return render(request, 'daftarclient.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def ubahpassuser(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            user.set_password(password_1)
            user.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('detailclient')

    context = {'form':form, 'act':'klien'}
    return render(request, 'ubahpassuser.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tambahuser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='client')
            # user.groups.add(group)
            # Client.objects.create(
            #     user=user,
            # )

            messages.success(request, 'Data Berhasil Ditambahkan untuk ' + username)
            return redirect('tambahclient')

    context = {'form':form, 'act':'klien'}
    return render(request, 'tambah_user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def tambahclient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('daftarclient')

    context = {'form':form, 'act':'klien'}
    return render(request, 'tambah_client.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detailclient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('daftarclient')

    context = {'client':client, 'form':form, 'act':'klien'}
    return render(request, 'detailclient.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm()

    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Data Berhasil Dihapus')
        return redirect('daftarclient')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def delklien(request, pk):
#     client = Client.objects.get(id=pk)
#     if request.method == 'POST':
#         client.delete()
#         messages.success(request, 'Data Berhasil Dihapus')
#         return redirect('daftarclient')
#
#     context = {'item':client, 'act':'klien'}
#     return render(request, 'del_client.html', context)
