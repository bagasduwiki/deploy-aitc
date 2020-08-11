from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CreateUserForm
from pelayanan.models import *
from accounts.models import *
from .decorators import allowed_users, admin_only

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                group = Group.objects.get(name='client')
                user.groups.add(group)
                # Client.objects.create(
                #     user=user,
                # )

                messages.success(request, 'Account was created for ' + username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)

    return redirect('login')

###############Dashboard########################################################
@login_required(login_url='login')
@admin_only
def home(request):
    pengaduan = Pengaduans.objects.all()
    client = Client.objects.all()

    tot_client = client.count()
    tot_pengaduan = pengaduan.count()
    tot_selesai = pengaduan.filter(kategori_penanganan=(3)).count()
    tot_tkp = pengaduan.filter(kategori_penanganan=(1)).count()
    tot_online = pengaduan.filter(kategori_penanganan=(2)).count()
    tot_progres = tot_tkp + tot_online

    context = {'act':'dashboard', 'pengaduan':pengaduan, 'client':client, 'tot_client':tot_client, 'tot_pengaduan':tot_pengaduan, 'tot_selesai':tot_selesai, 'tot_progres':tot_progres}
    return render(request,'dashboard.html',context)

###############User Page########################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def userPage(request):
    context = {}
    return render(request, 'user_page.html', context)
