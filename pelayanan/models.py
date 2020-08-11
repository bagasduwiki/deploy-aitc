from django.db import models
from master.models import *
from accounts.models import *
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    pengaduan = models.ForeignKey('Pengaduans', null=True, on_delete=models.SET_NULL)
    sender = models.CharField(max_length=255 ,null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class Pengaduans(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    kategori_pengaduan = models.ForeignKey(KategoriPengaduan, null=True, on_delete=models.SET_NULL)
    keluhan = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    selesai = models.BooleanField(null=True)
    kategori_penanganan = models.ForeignKey(KategoriPenanganan, null=True, on_delete=models.SET_NULL)
    respon = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.keluhan

class Respons(models.Model):
    pengaduan = models.ForeignKey(Pengaduans, null=True, on_delete=models.SET_NULL)
    jawab = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
