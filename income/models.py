from django.db import models

# Create your models here.
class Income(models.Model):
    kategori = models.CharField(max_length=255)
    jumlah = models.CharField(max_length=255)
    keterangan = models.CharField(max_length=255)
    tanggal = models.DateTimeField(auto_now_add=True)