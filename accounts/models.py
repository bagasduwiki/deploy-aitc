from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, null=True)
    alamat = models.CharField(max_length=200, null=True)
    no_hp = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pict = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, null=True)
    no_hp = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    instansi = models.CharField(max_length=200, null=True, blank=True)
    alamat = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama
