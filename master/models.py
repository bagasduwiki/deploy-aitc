from django.db import models


# Create your models here.
class KategoriPengaduan(models.Model):
    nama_kategori = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama_kategori

class KategoriPenanganan(models.Model):
    nama_kategori = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nama_kategori
