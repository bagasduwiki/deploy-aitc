from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from aitc_service.views import *
from aitc_service.forms import *
from .forms import *
from .models import *
from .filters import *

# Create your views here.
###############Pengaduan########################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pelayanan(request):
    pengaduan = Pengaduans.objects.all()
    client = Client.objects.all()
    stat_online = pengaduan.filter(Q(kategori_penanganan=(2)) | Q(kategori_penanganan=(1)))

    myFilter = filterpenanganan(request.GET, queryset=stat_online)
    orders = myFilter.qs

    form = PelayananForm()
    formup = EditStatusForm()
    if request.method == 'POST':
        form = PelayananForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('pelayanan')

    context = {'pengaduan':pengaduan, 'client':client, 'myFilter':myFilter, 'orders':orders, 'act':'pelayanan', 'form':form, 'formup':formup, 'stat_online':stat_online}
    return render(request, 'pelayanan.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pengsel(request):
    pengaduan = Pengaduans.objects.all()
    client = Client.objects.all()
    selesai = pengaduan.filter(kategori_penanganan=(3))

    context = {'pengaduan':pengaduan, 'client':client, 'act':'pengsel', 'selesai':selesai}
    return render(request, 'pengsel.html', context)

@login_required(login_url='login')
def updateStatus(request):
	formup = EditStatusForm()

	if request.method =='POST':
		formup = EditStatusForm(request.POST)
		if formup.is_valid():
			idk = formup.cleaned_data['pk']
			kategori_penanganan = formup.cleaned_data['kategori_penanganan']

			Pengaduans.objects.filter(id=idk).update(kategori_penanganan=kategori_penanganan)

			return redirect('pelayanan')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def filterpelayanan(request):
    pelayananfilter = FilterForm()
    if request.method == 'GET':
        pelayananfilter = FilterForm(request.GET)
        if pelayananfilter.is_valid():
            kategori = pelayananfilter.cleaned_data['kategori_penanganan']

            pelayanan = Pengaduans.objects.filter(kategori_penanganan=kategori)

    context = {'pelayananfilter':pelayananfilter, 'kategori':kategori, 'act':'pelayanan'}
    return render(request, 'pelayanan.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def tambahpelayanan(request):
#     form = PelayananForm()
#     if request.method == 'POST':
#         form = PelayananForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Data Berhasil Ditambahkan')
#             return redirect('pelayanan')
#
#     context = {'form':form, 'act':'pelayanan'}
#     return render(request, 'tambah_pelayanan.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def editstatus(request, pk):
    pengaduan = Pengaduans.objects.get(id=pk)
    form = StatusForm(instance=pengaduan)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=pengaduan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('pelayanan')

    context = {'form':form, 'pengaduan':pengaduan, 'act':'pelayanan'}
    return render(request, 'edit_status.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detailpelayanan(request, pk):
    pengaduan = Pengaduans.objects.get(id=pk)
    chatdata = Chat.objects.filter(pengaduan=pk)
    # respon = Respons.objects.get(id=pk)
    form = PelayananForm(instance=pengaduan)
    formchat = ChatForm(initial={'pengaduan':pengaduan, 'sender':request.user})

    if request.method == 'POST':
        form = PelayananForm(request.POST, instance=pengaduan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('detailpelayanan')

    context = {'pengaduan':pengaduan, 'form':form, 'act':'pelayanan', 'formchat':formchat, 'chatdata':chatdata}
    return render(request, 'detail_pelayanan.html', context)

def sendchat(request):
    if request.method == 'POST':
        formchat = ChatForm(request.POST)
        if formchat.is_valid():
            formchat.save()
            return JsonResponse({"success":True}, status=200)
        else:
            return JsonResponse({"success":False}, status=400)

def getchat(request):
    if request.is_ajax():
        chatdata = Chat.objects.filter(pengaduan=request.GET.get('pengaduan'))
        context = {'chatdata': chatdata}
        return render(request, 'partialchat.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def respon(request, pk):
	pengaduan = Pengaduans.objects.filter(id=pk)
	pengaduan1 = Pengaduans.objects.get(id=pk)
	pengaduan2 = Pengaduans.objects.all()
	respon = Respons.objects.filter(pengaduan=pk).order_by("-created_at")
	form = JawabForm(initial={'pengaduan':pengaduan1})

	if request.method == 'POST':
        # print('Printing post: ', request.POST)
		formset = JawabForm(request.POST)
		if formset.is_valid():
			formset.save()
			return redirect('pelayanan')

	context = {'pengaduan': pengaduan, 'pengaduan2':pengaduan2, 'act':'pelayanan', 'respon': respon, 'form':form}
	return render(request, 'detail_pelayanan.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletepelayanan(request, pk):
    pengaduan = Pengaduans.objects.get(id=pk)
    form = DeletePelayananForm()

    if request.method == 'POST':
        pengaduan.delete()
        messages.success(request, 'Data Berhasil Dihapus')
        return redirect('pelayanan')

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def pelayanandel(request, pk):
#     pengaduan = Pengaduans.objects.get(id=pk)
#     if request.method == 'POST':
#         pengaduan.delete()
#         messages.success(request, 'Data Berhasil Dihapus')
#         return redirect('pelayanan')
#
#     context = {'item':pengaduan, 'act':'pelayanan'}
#     return render(request, 'del_pelayanan.html', context)

###############Dashboard########################################################
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def detaildaftar(request, pk):
    pengaduan = Pengaduans.objects.get(id=pk)
    chatdata = Chat.objects.filter(pengaduan=pk)
    # respon = Respons.objects.get(id=pk)
    form = PelayananForm(instance=pengaduan)
    formchat = ChatForm(initial={'pengaduan':pengaduan, 'sender':request.user})

    context = {'form':form, 'pengaduan':pengaduan, 'act':'dashboard', 'formchat':formchat, 'chatdata':chatdata}
    return render(request, 'detail_daftar.html', context)
