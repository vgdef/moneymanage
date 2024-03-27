from django.db import models

# Create your models here.
class Income(models.Model):
    kategori = models.CharField(max_length=255)
    jumlah = models.CharField(max_length=255)
    keterangan = models.CharField(max_length=255)
    tanggal = models.DateTimeField(auto_now_add=True)

class Reference(models.Model):
    nama = models.CharField(max_length=255)
    jenis = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=1)